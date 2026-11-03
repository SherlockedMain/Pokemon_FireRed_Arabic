#!/usr/bin/env python3
"""Apply a translation batch to the source.

    python3 tools/arabic/apply_translations.py intro            # Arabic from the review sheet
    python3 tools/arabic/apply_translations.py intro --defaults # Arabic from translations/intro.py

Reads the Arabic from translations/<batch>.xlsx (column "Arabic"), wraps it
to each box's real pixel width, shapes it, writes it into the .inc / .c
files, and refreshes the sheet's Preview and Fit columns. Nothing is written
to the source for a row that does not fit; the script lists those rows.
"""
import importlib, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'translations'))
from arabic_text import wrap_pairs, measure, paragraphs, shape, ROOT

def layout(entry, ar):
    """-> (pieces, preview_lines, problems). pieces = [(shaped_line, sep)], sep in '\\n', '\\p', ''."""
    mode, max_px, font, max_lines = entry['box']
    problems, pieces, preview = [], [], []

    def check(shaped, readable):
        w = measure(shaped, font)
        if w > max_px:
            problems.append('"%s" is %d px, max %d' % (readable.strip(), w, max_px))

    ar = ar.replace('\r', '').strip('\n')
    if mode in ('line', 'manual'):
        for raw in ar.split('\n'):
            s = shape(raw)
            check(s, raw)
            pieces.append((s, '\n')); preview.append(raw)
        if len(pieces) > max_lines:
            problems.append('%d lines, max %d' % (len(pieces), max_lines))
    elif mode == 'dialog':
        pages = []
        for para in paragraphs(ar):
            lines = wrap_pairs(para, max_px, font)
            for i in range(0, len(lines), max_lines):
                pages.append(lines[i:i + max_lines])
        for pi, page in enumerate(pages):
            for li, (s, r) in enumerate(page):
                check(s, r)
                pieces.append((s, '\n' if li < len(page) - 1 else '\\p'))
                preview.append(r)
            if pi < len(pages) - 1:
                preview.append('   ———')
    else:  # static / help
        lines = []
        for pi, para in enumerate(paragraphs(ar)):
            if pi and mode == 'static':
                lines.append(('', ''))
            lines += wrap_pairs(para, max_px, font)
        for s, r in lines:
            check(s, r)
            pieces.append((s, '\n')); preview.append(r)
        if len(lines) > max_lines:
            problems.append('%d lines, max %d' % (len(lines), max_lines))
    # last separator: page prompt if the English had one, else nothing
    pieces[0] = (entry.get('prefix', '') + pieces[0][0], pieces[0][1])
    pieces[-1] = (pieces[-1][0] + entry.get('suffix', ''), '\\p' if entry.get('end') == 'p' else '')
    return pieces, preview, problems

def to_inc(pieces, indent):
    out = []
    for i, (s, sep) in enumerate(pieces):
        sep = '\\n' if sep == '\n' else sep
        out.append('%s.string "%s%s%s"' % (indent, s, sep, '$' if i == len(pieces) - 1 else ''))
    return '\n'.join(out) + '\n'

def to_c(pieces):
    return ''.join(s + ('\\n' if sep == '\n' else sep) for s, sep in pieces)

def write_entry(entry, pieces):
    if entry.get('codes'):   # {X1}, {X2}... stand for control codes written in the source
        pieces = [(re.sub(r'\{(X\d)\}', lambda k: entry['codes'][k.group(1)], s_), sep) for s_, sep in pieces]
    path = os.path.join(ROOT, entry['file'])
    src = open(path, encoding='utf-8').read()
    label = entry['id']
    if entry.get('ifdef'):
        # A string with #ifdef branches: the whole text is written into every
        # branch, with {X1}, {X2}... replaced by that branch's control codes.
        m = re.search(r'^%s::\n((?:(?:[ \t]*\.string .*|#if.*|#else.*|#endif.*)\n)+)' % re.escape(label), src, re.M)
        if not m:
            raise SystemExit('label %s not found in %s' % (label, entry['file']))
        heads = [l for l in m.group(1).split('\n') if l.startswith('#')]
        out = []
        for head, codes in zip(heads, entry['ifdef']):
            out.append(head)
            branch = [(re.sub(r'\{X(\d)\}', lambda k: codes[int(k.group(1)) - 1], s_), sep) for s_, sep in pieces]
            out.append(to_inc(branch, '    ').rstrip('\n'))
        out.append('#endif')
        src = src[:m.start(1)] + '\n'.join(out) + '\n' + src[m.end(1):]
    elif path.endswith(('.inc', '.s')):
        m = re.search(r'^%s::\n((?:[ \t]*\.string .*\n)+)' % re.escape(label), src, re.M)
        if not m:
            raise SystemExit('label %s not found in %s' % (label, entry['file']))
        indent = re.match(r'[ \t]*', m.group(1)).group(0)
        src = src[:m.start(1)] + to_inc(pieces, indent) + src[m.end(1):]
    else:
        m = re.search(r'\b%s\[\] = _\("(.*?)"\);' % re.escape(label), src)
        if not m:
            raise SystemExit('label %s not found in %s' % (label, entry['file']))
        src = src[:m.start(1)] + to_c(pieces) + src[m.end(1):]
    open(path, 'w', encoding='utf-8').write(src)

def sheet_path(batch):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'translations', batch + '.xlsx')

def main():
    batch = sys.argv[1]
    entries = importlib.import_module(batch).ENTRIES
    use_sheet = '--defaults' not in sys.argv and os.path.exists(sheet_path(batch))
    wb = ws = None
    if use_sheet:
        import openpyxl
        wb = openpyxl.load_workbook(sheet_path(batch))
        ws = wb['Translation']
        head = {c.value: c.column for c in ws[1]}
        rows = {ws.cell(r, head['ID']).value: r for r in range(2, ws.max_row + 1)}
    bad = 0
    for e in entries:
        ar = e['ar']
        if use_sheet and e['id'] in rows:
            ar = ws.cell(rows[e['id']], head['Arabic']).value or ''
        pieces, preview, problems = layout(e, ar)
        if use_sheet and e['id'] in rows:
            r = rows[e['id']]
            ws.cell(r, head['On-screen preview']).value = '\n'.join(preview)
            ws.cell(r, head['Fit']).value = 'OK' if not problems else 'TOO LONG: ' + '; '.join(problems)
        if problems:
            bad += 1
            print('DOES NOT FIT  %-40s %s' % (e['id'], '; '.join(problems)))
            continue
        write_entry(e, pieces)
    if wb:
        screens = os.path.join(os.path.dirname(sheet_path(batch)), batch + '_screens')
        if 'Screens' in wb.sheetnames and os.path.isdir(screens):
            from make_sheet import add_screens
            add_screens(wb['Screens'], screens)
        wb.save(sheet_path(batch))
    print('%d strings written, %d skipped (too long)' % (len(entries) - bad, bad))
    return bad

if __name__ == '__main__':
    sys.exit(1 if main() else 0)
