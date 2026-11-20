import subprocess
import uuid
from pathlib import Path
import math

PCB_DIR = Path(r"C:\Antigravity\PRISM SAFETY GPS\cad_eda\02_KiCad_Schematic_PCB")
PRETTY_DIR = PCB_DIR / "PRISM_Safety_GPS.pretty"
pcb_file = PCB_DIR / "PRISM_SAFETY_GPS.kicad_pcb"

def u():
    return str(uuid.uuid4())

X0, Y0 = 100.0, 100.0
W, H = 60.0, 40.0
PITCH = 2.54
COLS, ROWS = 22, 15
OX = X0 + (W - (COLS - 1) * PITCH) / 2.0  # 103.33
OY = Y0 + (H - (ROWS - 1) * PITCH) / 2.0  # 102.22

corners = [(X0 + 3.0, Y0 + 3.0), (X0 + W - 3.0, Y0 + 3.0), (X0 + 3.0, Y0 + H - 3.0), (X0 + W - 3.0, Y0 + H - 3.0)]

def dist(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Build Footprint file
fp_pads = []
pad_idx = 1
for r_idx in range(ROWS):
    for c_idx in range(COLS):
        abs_x = OX + c_idx * PITCH
        abs_y = OY + r_idx * PITCH
        too_close = False
        for cx, cy in corners:
            if dist((abs_x, abs_y), (cx, cy)) < 2.8:
                too_close = True
                break
        if too_close:
            continue
        rel_x = round(abs_x - (X0 + W/2.0), 3)
        rel_y = round(abs_y - (Y0 + H/2.0), 3)
        fp_pads.append(f'\t\t(pad "{pad_idx}" thru_hole circle (at {rel_x} {rel_y}) (size 1.6 1.6) (drill 0.9) (layers "*.Cu" "*.Mask"))')
        pad_idx += 1

fp_lines = [
    '(footprint "Perfboard_Matrix_60x40"',
    '\t(version 20240108)',
    '\t(generator "kicad_pcb_editor")',
    '\t(generator_version "10.0")',
    '\t(layer "F.Cu")',
    '\t(property "Reference" "BRD" (at 0 0 0) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))',
    '\t(property "Value" "Perfboard_Matrix_60x40" (at 0 0 0) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))',
] + fp_pads + [')']

(PRETTY_DIR / "Perfboard_Matrix_60x40.kicad_mod").write_text("\n".join(fp_lines), encoding="utf-8")

# Build kicad_pcb
lines = [
    '(kicad_pcb',
    '\t(version 20240108)',
    '\t(generator "pcbnew")',
    '\t(generator_version "10.0")',
    '\t(general',
    '\t\t(thickness 1.6)',
    '\t\t(legacy_teardrops no)',
    '\t)',
    '\t(paper "A4")',
    '\t(title_block',
    '\t\t(title "PRISM SAFETY GPS - Perfboard 60x40mm Solder Matrix & Components")',
    '\t\t(date "2026-11-05")',
    '\t\t(rev "1.0")',
    '\t\t(company "Universitas Muhammadiyah Prof. DR. HAMKA (FTII UHAMKA)")',
    '\t\t(comment 1 "Author: Ahmad Rifa\'i Wibisono (NIM: 2201015024)")',
    '\t\t(comment 2 "Project: PRJ-PSG-01 | Third Angle Projection | ISO 2768-m")',
    '\t\t(comment 3 "Matrix 22x15 Pitch 2.54mm | Direct Pad Soldering Z <= 3.2mm")',
    '\t)',
    '\t(layers',
    '\t\t(0 "F.Cu" signal)',
    '\t\t(31 "B.Cu" signal)',
    '\t\t(36 "B.SilkS" user "B.Silkscreen")',
    '\t\t(37 "F.SilkS" user "F.Silkscreen")',
    '\t\t(38 "B.Mask" user)',
    '\t\t(39 "F.Mask" user)',
    '\t\t(44 "Edge.Cuts" user)',
    '\t)',
    '\t(setup',
    '\t\t(pad_to_mask_clearance 0.05)',
    '\t\t(solder_mask_min_width 0.1)',
    '\t)',
    '\t(net 0 "")',
    f'\t(gr_rect (start {X0} {Y0}) (end {X0+W} {Y0+H}) (stroke (width 0.15) (type solid)) (fill none) (layer "Edge.Cuts") (uuid "{u()}"))',
]

for cx, cy in corners:
    lines.append(f'\t(footprint "PRISM_Safety_GPS:MountingHole_M2" (layer "F.Cu") (at {cx} {cy}) (uuid "{u()}")')
    lines.append(f'\t\t(property "Reference" "H" (at 0 0 0) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))')
    lines.append(f'\t\t(property "Value" "MountingHole_M2" (at 0 0 0) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))')
    lines.append(f'\t\t(pad "" np_thru_hole circle (at 0 0) (size 2.2 2.2) (drill 2.2) (layers "*.Cu" "*.Mask"))')
    lines.append('\t)')

# Place Perfboard Matrix footprint with matching pads
lines.append(f'\t(footprint "PRISM_Safety_GPS:Perfboard_Matrix_60x40" (layer "F.Cu") (at {X0+W/2.0} {Y0+H/2.0}) (uuid "{u()}")')
lines.append(f'\t\t(property "Reference" "BRD1" (at 0 0 0) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))')
lines.append(f'\t\t(property "Value" "Perfboard_Matrix_60x40" (at 0 0 0) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))')
lines.extend(fp_pads)
lines.append('\t)')

# Silk markings along border (placed on F.Fab / Dwgs.User to avoid pad solder mask clipping)
for r_idx, r_char in enumerate("ABCDEFGHIJKLMNO"):
    y = 102.22 + r_idx * 2.54
    lines.append(f'\t(gr_text "{r_char}" (at {X0+1.2} {y} 0) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.15))) (uuid "{u()}"))')
    lines.append(f'\t(gr_text "{r_char}" (at {X0+W-1.2} {y} 0) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.15))) (uuid "{u()}"))')

for c_idx in range(22):
    x = 103.33 + c_idx * 2.54
    lines.append(f'\t(gr_text "{c_idx+1}" (at {x} {Y0+1.0} 0) (layer "F.Fab") (effects (font (size 0.8 0.8) (thickness 0.15))) (uuid "{u()}"))')
    lines.append(f'\t(gr_text "{c_idx+1}" (at {x} {Y0+H-1.0} 0) (layer "F.Fab") (effects (font (size 0.8 0.8) (thickness 0.15))) (uuid "{u()}"))')

lines.append(')')

pcb_file.write_text("\n".join(lines), encoding="utf-8")

kicad_cli = r"C:\Program Files\KiCad\10.0\bin\kicad-cli.exe"
rpt = PCB_DIR / "drc_perfboard.rpt"
res = subprocess.run([kicad_cli, "pcb", "drc", "--severity-all", "--exit-code-violations", "--output", str(rpt), str(pcb_file)], capture_output=True, text=True)
print("DRC Exit:", res.returncode)
if rpt.exists():
    text = rpt.read_text(encoding="utf-8")
    for l in text.splitlines()[:25]:
        print(" ", l)
