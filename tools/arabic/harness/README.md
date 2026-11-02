# Headless screenshot harness

Plays a ROM in mGBA without a window, following a script of button presses,
and saves screenshots. Used to check every translated screen.

    sudo apt install libmgba-dev          # or build mGBA from source
    gcc -O1 -o run run.c -lmgba
    mkdir -p out && ./run ../../../pokefirered.gba intro_walkthrough.txt out
    python3 to_png.py out                 # .raw frames -> 2x PNGs

Script commands, one per line:

- `wait N`: run N frames with no buttons held
- `press KEYS [frames]`: hold KEYS (A, B, START, SELECT, UP, DOWN, LEFT, RIGHT, L, R; combine with +), default 4 frames
- `shot NAME`: save the current frame as NAME.raw

The walkthroughs start from a fresh ROM with no save file.
