import subprocess
from pathlib import Path
import math

PCB_DIR = Path(r"C:\Antigravity\PRISM SAFETY GPS\cad_eda\02_KiCad_Schematic_PCB")
PRETTY_DIR = PCB_DIR / "PRISM_Safety_GPS.pretty"

X0, Y0 = 100.0, 100.0
W, H = 60.0, 40.0
PITCH = 2.54
COLS, ROWS = 22, 15
OX = X0 + (W - (COLS - 1) * PITCH) / 2.0  # 103.33
OY = Y0 + (H - (ROWS - 1) * PITCH) / 2.0  # 102.22

ROW_LETTERS = "ABCDEFGHIJKLMNO"

# Mounting holes
corners = [(X0 + 3.0, Y0 + 3.0), (X0 + W - 3.0, Y0 + 3.0), (X0 + 3.0, Y0 + H - 3.0), (X0 + W - 3.0, Y0 + H - 3.0)]

def dist(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Build Perfboard Footprint
fp_lines = [
    '(footprint "Perfboard_Matrix_60x40"',
    '\t(version 20240108)',
    '\t(generator "kicad_pcb_editor")',
    '\t(generator_version "10.0")',
    '\t(layer "F.Cu")',
    '\t(property "Reference" "REF**" (at 0 -2 0) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))',
    '\t(property "Value" "Perfboard_Matrix_60x40" (at 0 2 0) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))',
]

# Add pads to footprint (relative to board center: 30, 20)
pad_idx = 1
for r_idx in range(ROWS):
    for c_idx in range(COLS):
        # absolute pos
        abs_x = OX + c_idx * PITCH
        abs_y = OY + r_idx * PITCH
        # check distance to any corner mounting hole
        too_close = False
        for cx, cy in corners:
            if dist((abs_x, abs_y), (cx, cy)) < 2.8:
                too_close = True
                break
        if too_close:
            continue
        rel_x = round(abs_x - (X0 + W/2.0), 3)
        rel_y = round(abs_y - (Y0 + H/2.0), 3)
        fp_lines.append(f'\t(pad "{pad_idx}" thru_hole circle (at {rel_x} {rel_y}) (size 1.6 1.6) (drill 0.9) (layers "*.Cu" "*.Mask"))')
        pad_idx += 1

fp_lines.append(')')
(PRETTY_DIR / "Perfboard_Matrix_60x40.kicad_mod").write_text("\n".join(fp_lines), encoding="utf-8")
print(f"Footprint Perfboard_Matrix_60x40 created with {pad_idx-1} pads.")
