#!/usr/bin/env python3
"""Build the review workbook for a translation batch.

    python3 tools/arabic/make_sheet.py intro [--vanilla PATH] [--screens DIR]

Sheets: Read me, Translation (the Arabic column is the source of truth that
apply_translations.py reads), Glossary, Screens (emulator screenshots).
English is read from an untouched pokefirered checkout (--vanilla).
"""
import argparse, importlib, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, 'translations'))
from apply_translations import layout, sheet_path
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.formatting.rule import FormulaRule
from openpyxl.drawing.image import Image as XLImage

FONT = 'Arial'
HEAD_FILL = PatternFill('solid', start_color='1F4E78')
EDIT_FILL = PatternFill('solid', start_color='FFF2CC')
THIN = Side(style='thin', color='BFBFBF')
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

def english(vanilla, entry):
    if entry.get('json'):
        data = json.load(open(os.path.join(vanilla, entry['file']), encoding='utf-8'))
        key = entry.get('json_key', 'itemId')
        rows = data[entry.get('json_list', 'items')]
        v = next(i for i in rows if i.get(key, i.get(entry['json_field'])) == entry['json'])[entry['json_field']]
        return v.replace('\\\\n', '\n').replace('\\n', '\n')
    src = open(os.path.join(vanilla, entry['file']), encoding='utf-8').read()
    if entry['file'].endswith(('.inc', '.s')):
        m = re.search(r'^%s::\n((?:(?:[ \t]*\.string .*|#if.*|#else.*|#endif.*)\n)+)' % re.escape(entry['id']), src, re.M)
        body = m.group(1)
        if '#else' in body:   # show one branch (the retail one) plus the shared tail
            body = re.sub(r'#if.*?\n(.*?)#else.*?\n.*?#endif.*?\n', lambda k: '', body, flags=re.S) + body
            body = re.sub(r'#if.*?#else.*?\n', '', m.group(1), flags=re.S).replace('#endif\n', '')
        text = ''.join(re.findall(r'\.string "(.*)"', body))
        text = re.sub(r'\{(COLOR|FONT|PLAY_BGM|MUS_|PAUSE|RESUME_MUSIC)[^}]*\}', '', text)
    elif entry.get('key'):
        text = re.search(entry.get('pattern', r'\[%s\]\s*=\s*_\("(.*?)"\)') % re.escape(entry['key']), src).group(1)
    else:
        m = re.search(r'\b%s\[\] = _\("(.*?)"\);' % re.escape(entry['id']), src)
        if not m:
            mm = re.search(r'\b%s\[\] = _\((.*?)\);' % re.escape(entry['id']), src, re.S)
            if mm:
                return ''.join(re.findall(r'"((?:[^"\\]|\\.)*)"', mm.group(1))).replace('\\n', '\n')
        if not m:                      # a string added by the translation (not in the original game)
            return '(new in the Arabic version)'
        text = m.group(1)
    text = text.rstrip('$').replace('\\p', '\n\n').replace('\\n', '\n').replace('\\l', '\n')
    return text.strip('\n')

def box_text(box):
    mode, px, font, lines = box
    small = ' (small font)' if font == 'small' else ''
    return {'dialog': 'Dialogue box: pages of %d lines, %d px per line' % (lines, px),
            'static': 'Fixed screen: up to %d lines, %d px per line' % (lines, px),
            'help':   'HELP panel: up to %d lines, %d px per line' % (lines, px),
            'line':   'One line, %d px%s' % (px, small),
            'manual': 'Lines exactly as written: up to %d, %d px each%s' % (lines, px, small),
            'steps': 'Numbered steps ({CIRCLE_n}), re-wrapped to %d px; up to %d lines%s' % (px, lines, small)}[mode]

def style_header(ws, headers, widths):
    for c, (h, w) in enumerate(zip(headers, widths), 1):
        cell = ws.cell(1, c, h)
        cell.font = Font(name=FONT, bold=True, color='FFFFFF')
        cell.fill = HEAD_FILL
        cell.alignment = Alignment(vertical='center', wrap_text=True)
        cell.border = BORDER
        ws.column_dimensions[cell.column_letter].width = w
    ws.freeze_panes = 'A2'
    ws.row_dimensions[1].height = 30

def add_screens(ws, folder):
    """(Re)fill the Screens sheet. openpyxl drops images when it re-saves a
    workbook, so apply_translations.py calls this again after editing."""
    ws._images = []
    ws.column_dimensions['A'].width = 36
    ws.column_dimensions['B'].width = 70
    shots = json.load(open(os.path.join(folder, 'screens.json'), encoding='utf-8'))
    ws.cell(1, 1, 'Screenshots from the patched ROM (mGBA, headless), in play order.').font = Font(name=FONT, bold=True, size=12)
    r = 3
    for fname, caption in shots:
        c = ws.cell(r, 1, caption); c.font = Font(name=FONT, size=10)
        c.alignment = Alignment(wrap_text=True, vertical='top')
        img = XLImage(os.path.join(folder, fname)); img.width, img.height = 480, 320
        ws.add_image(img, 'B%d' % r)
        for k in range(r, r + 17):
            ws.row_dimensions[k].height = 19
        r += 18

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('batch')
    ap.add_argument('--vanilla', default=os.path.join(HERE, '..', '..', '..', 'vanilla'))
    ap.add_argument('--screens')
    a = ap.parse_args()
    mod = importlib.import_module(a.batch)
    wb = Workbook()

    # ---- Read me
    ws = wb.active; ws.title = 'Read me'
    ws.column_dimensions['A'].width = 110
    lines = getattr(mod, 'README', [])
    for r, (text, kind) in enumerate(lines, 1):
        c = ws.cell(r, 1, text)
        c.font = Font(name=FONT, bold=kind in ('title', 'head'), size=14 if kind == 'title' else 11)
        c.alignment = Alignment(wrap_text=True, vertical='top')
        if kind == 'edit':
            c.fill = EDIT_FILL

    # ---- Translation
    ws = wb.create_sheet('Translation')
    headers = ['#', 'ID', 'Screen', 'Where it appears', 'Box', 'English', 'Arabic',
               'On-screen preview', 'Fit', 'Translator notes', 'Your comments']
    style_header(ws, headers, [5, 30, 16, 26, 22, 42, 46, 46, 16, 44, 30])
    for i, e in enumerate(mod.ENTRIES, 1):
        pieces, preview, problems = layout(e, e['ar'])
        row = [i, e['id'], e['screen'], e['where'], box_text(e['box']), english(a.vanilla, e), e['ar'],
               '\n'.join(preview), 'OK' if not problems else 'TOO LONG: ' + '; '.join(problems), e.get('note', ''), '']
        r = i + 1
        for c, v in enumerate(row, 1):
            cell = ws.cell(r, c, v)
            cell.font = Font(name=FONT, size=12 if c in (7, 8) else 10)
            cell.border = BORDER
            rtl = c in (7, 8)
            cell.alignment = Alignment(wrap_text=True, vertical='top',
                                       horizontal='right' if rtl else 'left', readingOrder=2 if rtl else 0)
            if c == 7:
                cell.fill = EDIT_FILL
        n = max(len(str(row[5]).split('\n')), len(row[7].split('\n')), 1)
        ws.row_dimensions[r].height = min(400, 18 * n + 6)
    last = len(mod.ENTRIES) + 1
    ws.conditional_formatting.add('I2:I%d' % last, FormulaRule(formula=['LEFT($I2,2)="OK"'],
                                  fill=PatternFill('solid', start_color='C6EFCE'), font=Font(color='006100')))
    ws.conditional_formatting.add('I2:I%d' % last, FormulaRule(formula=['LEFT($I2,3)="TOO"'],
                                  fill=PatternFill('solid', start_color='FFC7CE'), font=Font(color='9C0006')))
    ws.auto_filter.ref = 'A1:K%d' % last

    # ---- Glossary
    ws = wb.create_sheet('Glossary')
    style_header(ws, ['English', 'Arabic', 'Why', 'Your decision'], [26, 26, 80, 30])
    for r, (en, ar, why) in enumerate(getattr(mod, 'GLOSSARY', []), 2):
        for c, v in enumerate([en, ar, why, ''], 1):
            cell = ws.cell(r, c, v)
            cell.font = Font(name=FONT, size=12 if c == 2 else 10)
            cell.border = BORDER
            cell.alignment = Alignment(wrap_text=True, vertical='top', horizontal='right' if c == 2 else 'left',
                                       readingOrder=2 if c == 2 else 0)
            if c == 4:
                cell.fill = EDIT_FILL

    # ---- Screens
    screens = a.screens or os.path.join(HERE, 'translations', a.batch + '_screens')
    if os.path.isdir(screens):
        add_screens(wb.create_sheet('Screens'), screens)
    wb.save(sheet_path(a.batch))
    print('wrote', sheet_path(a.batch))

if __name__ == '__main__':
    main()
