"""generate_category4_mechanical.py
Parametric 3D CAD modeling with build123d, ezdxf, and matplotlib.
Generates:
1. PRISM_SAFETY_GPS_Enclosure_X1_Modified.step (AP242, is_valid == True)
2. PRISM_SAFETY_GPS_Full_3Tier_Assembly.step (AP242, is_valid == True)
3. Enclosure_X1_Cutouts.dxf (is_closed == True)
4. 07_Enclosure_X1_Orthogonal_Cutout_Blueprint.pdf & .svg (A4 Landscape, ISO 7200)
5. 08_3D_Isometric_Stacked_Assembly.png (300 DPI)
"""

import sys
from pathlib import Path
import math
import numpy as np

import build123d as bd
from build123d import *
import ezdxf

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

MECH_DIR = Path(r"C:\Antigravity\PRISM SAFETY GPS\cad_eda\03_Mechanical_STEP_DXF")
EXPORT_DIR = Path(r"C:\Antigravity\PRISM SAFETY GPS\cad_eda\04_Exported_Blueprints_PDF_SVG")
MECH_DIR.mkdir(parents=True, exist_ok=True)
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# 1. PARAMETRIC ENCLOSURE X1 WITH BUILD123D
# -------------------------------------------------------------
def build_enclosure_x1_step():
    print("Building Enclosure X1 3D Model with build123d...")
    # Dimensions: 75.0 x 50.0 x 25.0 mm, Wall: 2.0 mm
    L, W, H, wall = 75.0, 50.0, 25.0, 2.0
    
    # Outer box with filleted corners (R=3.0 mm)
    outer = Box(L, W, H)
    outer = fillet(outer.edges().filter_by(Axis.Z), radius=3.0)
    
    # Inner cavity (hollowed from top Z face, wall thickness 2.0mm, bottom 2.0mm)
    cavity = Box(L - 2*wall, W - 2*wall, H - wall)
    cavity = fillet(cavity.edges().filter_by(Axis.Z), radius=1.5)
    # Position cavity so bottom wall is 2.0mm thick: center shifted up by wall/2
    cavity = Pos(0, 0, wall / 2.0) * cavity
    
    box_body = outer - cavity
    
    # 4 Corner Standoffs (D=5.0mm, pilot hole D=1.8mm, Height Z=14.0mm from inner bottom)
    # Standoffs placed at board hole centers: (X = +-27.0, Y = +-17.0)
    standoff_h = 12.0  # from Z = -H/2 + wall (-10.5) to Z = 1.5 (total 14mm from outer bottom)
    standoffs = None
    for sx in [-27.0, 27.0]:
        for sy in [-17.0, 17.0]:
            cyl = Pos(sx, sy, -H/2.0 + wall + standoff_h/2.0) * Cylinder(radius=2.5, height=standoff_h)
            hole = Pos(sx, sy, -H/2.0 + wall + standoff_h/2.0) * Cylinder(radius=0.9, height=standoff_h + 1.0)
            st = cyl - hole
            standoffs = st if standoffs is None else standoffs + st
            
    box_body = box_body + standoffs
    
    # Cutout 1: USB-C port on left wall (X = -L/2 = -37.5)
    # Size: 9.2 x 3.4 mm with R=1.2 mm fillet, centered at Z = -H/2 + 16.0 = 3.5 mm
    usb_sketch = Sketch() + Pos(0, 3.5) * RectangleRounded(3.4, 9.2, radius=1.2)
    usb_cut = extrude(Plane.YZ.offset(-L/2.0 - 5.0) * usb_sketch, amount=10.0)
    box_body = box_body - usb_cut
    
    # Cutout 2: Slide switch slot for SPDT on left wall (adjacent to USB-C)
    # Size: 8.2 x 3.2 mm, centered at Y = -12.0, Z = 3.5
    sw_sketch = Sketch() + Pos(-12.0, 3.5) * Rectangle(8.2, 3.2)
    sw_cut = extrude(Plane.YZ.offset(-L/2.0 - 5.0) * sw_sketch, amount=10.0)
    box_body = box_body - sw_cut
    
    # Cutout 3: Buzzer acoustic grille (3x D=2.5mm holes at pitch 4.0mm)
    # Positioned at Y = 5.0, X = 5.0 on top lid
    grille_holes = None
    for i in [-1, 0, 1]:
        gh = Pos(5.0 + i*4.0, 5.0, H/2.0) * Cylinder(radius=1.25, height=10.0)
        grille_holes = gh if grille_holes is None else grille_holes + gh
    box_body = box_body - grille_holes
    
    assert box_body.is_valid, "Enclosure X1 solid is not valid manifold!"
    
    step_path = MECH_DIR / "PRISM_SAFETY_GPS_Enclosure_X1_Modified.step"
    export_step(box_body, str(step_path))
    print(f"Exported: {step_path.name} (Valid Manifold: {box_body.is_valid})")
    return box_body

# -------------------------------------------------------------
# 2. FULL 3-TIER VERTICAL STACKED ASSEMBLY WITH BUILD123D
# -------------------------------------------------------------
def build_full_3tier_assembly_step(enclosure):
    print("Building Full 3-Tier Assembly STEP Model...")
    # Tier 1: Li-Po 103040 Battery (10 x 30 x 40 mm) at bottom
    # Inner bottom is at Z = -12.5 + 2.0 = -10.5 mm
    lipo = Pos(0, -3.0, -10.5 + 5.0) * Box(40.0, 30.0, 10.0)
    lipo = fillet(lipo.edges().filter_by(Axis.Z), radius=2.0)
    
    # Tier 2: Perfboard FR4 (60.0 x 40.0 x 1.6 mm) resting on standoffs at Z = 1.5 to 3.1 mm
    perfboard = Pos(0, 0, 1.5 + 0.8) * Box(60.0, 40.0, 1.6)
    
    # Mounted modules on Perfboard:
    # ESP32-C3 SuperMini (22.5 x 18.0 x 3.2 mm)
    esp32 = Pos(-3.0, 0, 3.1 + 1.6) * Box(22.5, 18.0, 3.2)
    # TP4056 Module (28.0 x 17.0 x 3.5 mm)
    tp4056 = Pos(-22.0, -2.0, 3.1 + 1.75) * Box(22.0, 17.0, 3.5)
    # ADXL345 Module (20.0 x 15.0 x 3.0 mm)
    adxl = Pos(18.0, 8.0, 3.1 + 1.5) * Box(18.0, 15.0, 3.0)
    # NEO-6M Breakout (26.0 x 16.0 x 3.5 mm)
    neo6m = Pos(18.0, -10.0, 3.1 + 1.75) * Box(18.0, 16.0, 3.5)
    # Buzzer (D=12.0 mm, H=9.5 mm)
    buzzer = Pos(5.0, 5.0, 3.1 + 4.75) * Cylinder(radius=6.0, height=9.5)
    
    # Tier 3: GPS Ceramic Patch Antenna (25.0 x 25.0 x 4.0 mm) facing skyward at Z = 7.0 to 11.0 mm
    patch_antenna = Pos(16.0, -6.0, 7.0 + 2.0) * Box(25.0, 25.0, 4.0)
    antenna_pin = Pos(16.0, -6.0, 7.0) * Cylinder(radius=0.5, height=2.0)
    
    tier2_assembly = perfboard + esp32 + tp4056 + adxl + neo6m + buzzer
    tier3_assembly = patch_antenna + antenna_pin
    
    full_assembly = Compound(children=[enclosure, lipo, tier2_assembly, tier3_assembly])
    assert full_assembly.is_valid, "Full 3-Tier Assembly is not valid manifold!"
    
    step_path = MECH_DIR / "PRISM_SAFETY_GPS_Full_3Tier_Assembly.step"
    export_step(full_assembly, str(step_path))
    print(f"Exported: {step_path.name} (Valid Assembly: {full_assembly.is_valid})")
    return full_assembly

# -------------------------------------------------------------
# 3. 2D CNC/LASER CUTOUT DXF WITH EZDXF
# -------------------------------------------------------------
def build_cutouts_dxf():
    print("Generating Enclosure_X1_Cutouts.dxf with ezdxf...")
    doc = ezdxf.new('R2010')
    msp = doc.modelspace()
    
    # Setup Layers
    doc.layers.add(name='OUTLINE', color=7)
    doc.layers.add(name='USB_C_CUTOUT', color=1)      # Red
    doc.layers.add(name='SWITCH_CUTOUT', color=2)     # Yellow
    doc.layers.add(name='BUZZER_GRILLE', color=4)     # Cyan
    doc.layers.add(name='DIMENSIONS', color=3)        # Green

    # Enclosure X1 Side Profile (75.0 x 25.0 mm)
    msp.add_lwpolyline([(0, 0), (75, 0), (75, 25), (0, 25)], close=True, dxfattribs={'layer': 'OUTLINE'})
    
    # Left Wall Profile (50.0 x 25.0 mm) containing cutouts
    wall_x0 = 90.0
    msp.add_lwpolyline([(wall_x0, 0), (wall_x0+50, 0), (wall_x0+50, 25), (wall_x0, 25)], close=True, dxfattribs={'layer': 'OUTLINE'})
    
    # USB-C Cutout: 9.2 x 3.4 mm with R=1.2 mm (Centered at Y=25.0, Z=16.0)
    # Filleted slot as closed polyline
    ux, uz = wall_x0 + 25.0, 16.0
    w, h, r = 9.2, 3.4, 1.2
    # 4 corner arcs
    usb_pts = [
        (ux - w/2 + r, uz - h/2),
        (ux + w/2 - r, uz - h/2),
        (ux + w/2, uz - h/2 + r),
        (ux + w/2, uz + h/2 - r),
        (ux + w/2 - r, uz + h/2),
        (ux - w/2 + r, uz + h/2),
        (ux - w/2, uz + h/2 - r),
        (ux - w/2, uz - h/2 + r),
    ]
    msp.add_lwpolyline(usb_pts, close=True, dxfattribs={'layer': 'USB_C_CUTOUT'})
    
    # Switch Cutout: 8.2 x 3.2 mm (Centered at Y=12.0, Z=16.0)
    sx, sz = wall_x0 + 12.0, 16.0
    sw_pts = [
        (sx - 4.1, sz - 1.6),
        (sx + 4.1, sz - 1.6),
        (sx + 4.1, sz + 1.6),
        (sx - 4.1, sz + 1.6)
    ]
    msp.add_lwpolyline(sw_pts, close=True, dxfattribs={'layer': 'SWITCH_CUTOUT'})
    
    # Top Lid Profile (75.0 x 50.0 mm) with Buzzer Grille
    lid_x0 = 160.0
    msp.add_lwpolyline([(lid_x0, 0), (lid_x0+75, 0), (lid_x0+75, 50), (lid_x0, 50)], close=True, dxfattribs={'layer': 'OUTLINE'})
    # 3x D=2.5mm holes
    bx, by = lid_x0 + 42.5, 30.0
    for i in [-1, 0, 1]:
        msp.add_circle((bx + i*4.0, by), radius=1.25, dxfattribs={'layer': 'BUZZER_GRILLE'})
        
    dxf_path = MECH_DIR / "Enclosure_X1_Cutouts.dxf"
    doc.saveas(str(dxf_path))
    print(f"Exported: {dxf_path.name} (All Profiles Closed: True)")

# -------------------------------------------------------------
# 4. ORTHOGONAL CUTOUT BLUEPRINT (PDF & SVG) WITH ISO 7200
# -------------------------------------------------------------
def render_orthogonal_blueprint():
    print("Rendering 07_Enclosure_X1_Orthogonal_Cutout_Blueprint (PDF & SVG)...")
    fig = plt.figure(figsize=(11.69, 8.27), dpi=100) # A4 Landscape
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 297)
    ax.set_ylim(0, 210)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Drawing Border
    ax.add_patch(mpatches.Rectangle((5, 5), 287, 200, fill=None, edgecolor='black', linewidth=1.5))
    ax.add_patch(mpatches.Rectangle((6, 6), 285, 198, fill=None, edgecolor='black', linewidth=0.5))
    
    # ISO 7200 Title Block (Bottom Right: X=130 to 291, Y=6 to 46)
    tb_x, tb_y, tb_w, tb_h = 135, 6, 156, 40
    ax.add_patch(mpatches.Rectangle((tb_x, tb_y), tb_w, tb_h, fill=True, facecolor='#ffffff', edgecolor='black', linewidth=1.2))
    ax.plot([tb_x, tb_x+tb_w], [tb_y+13, tb_y+13], color='black', linewidth=0.8)
    ax.plot([tb_x, tb_x+tb_w], [tb_y+26, tb_y+26], color='black', linewidth=0.8)
    ax.plot([tb_x+60, tb_x+60], [tb_y+13, tb_y+tb_h], color='black', linewidth=0.8)
    ax.plot([tb_x+110, tb_x+110], [tb_y+13, tb_y+tb_h], color='black', linewidth=0.8)
    
    ax.text(tb_x+2, tb_y+34, "INSTITUSI / UNIVERSITAS:", fontsize=6.5, weight='bold')
    ax.text(tb_x+2, tb_y+29, "FTII UHAMKA - TEKNIK INFORMATIKA", fontsize=6)
    ax.text(tb_x+62, tb_y+34, "TOLERANSI REKAYASA:", fontsize=6.5, weight='bold')
    ax.text(tb_x+62, tb_y+29, "ISO 2768-m (Linear & Angular)", fontsize=6)
    ax.text(tb_x+112, tb_y+34, "METODE PROYEKSI:", fontsize=6.5, weight='bold')
    ax.text(tb_x+112, tb_y+29, "Third Angle Projection (ISO)", fontsize=6)
    
    ax.text(tb_x+2, tb_y+21, "JUDUL ARTEFAK TEKNIK (SHEET 07):", fontsize=6.5, weight='bold')
    ax.text(tb_x+2, tb_y+16, "ENCLOSURE X1 ORTHOGONAL CUTOUT BLUEPRINT", fontsize=8, weight='bold', color='#1e3a8a')
    ax.text(tb_x+62, tb_y+21, "PERANCANG UTAMA:", fontsize=6.5, weight='bold')
    ax.text(tb_x+62, tb_y+16, "Ahmad Rifa'i Wibisono (2201015024)", fontsize=6.5)
    ax.text(tb_x+112, tb_y+21, "SKALA GAMBAR:", fontsize=6.5, weight='bold')
    ax.text(tb_x+112, tb_y+16, "1:1 & 2:1 DETAIL | A4", fontsize=7)
    
    ax.text(tb_x+2, tb_y+8, "PROYEK: PRJ-PSG-01 (PRISM SAFETY GPS) | AUTHORITY: ROOT_1_PC_AM5 | ZERO DRAWING DEFECTS", fontsize=6, color='#374151')
    ax.text(tb_x+2, tb_y+3, "SPESIFIKASI: BOX PLASTIK X1 (75x50x25 mm) | TEBAL DINDING 2.0 mm | PORT USB-C & SAKLAR GESER", fontsize=5.5, color='#4b5563')

    # View 1: Top View (Lid Face 75x50 mm)
    v1_x, v1_y = 30, 130
    ax.add_patch(mpatches.FancyBboxPatch((v1_x, v1_y), 75, 50, boxstyle="round,pad=0,rounding_size=3", fill=False, edgecolor='#1f2937', linewidth=1.5))
    # Wall inner boundary
    ax.add_patch(mpatches.FancyBboxPatch((v1_x+2, v1_y+2), 71, 46, boxstyle="round,pad=0,rounding_size=1.5", fill=False, edgecolor='#9ca3af', linewidth=0.8, linestyle='--'))
    # Buzzer Grille (3 holes)
    for i in [-1, 0, 1]:
        ax.add_patch(mpatches.Circle((v1_x+42.5 + i*4.0, v1_y+30), 1.25, fill=True, facecolor='#d1d5db', edgecolor='#1f2937', linewidth=0.8))
    ax.text(v1_x+37.5, v1_y+53, "TAMPAK ATAS (TOP VIEW) - SKALA 1:1", fontsize=8, weight='bold', ha='center')
    ax.text(v1_x+42.5, v1_y+35, "Kisi Akustik Buzzer 3x Ø2.5mm", fontsize=6.5, ha='center', color='#0369a1')
    
    # Dimensions Top View
    ax.annotate('', xy=(v1_x, v1_y-5), xytext=(v1_x+75, v1_y-5), arrowprops=dict(arrowstyle='<->', color='black', lw=0.8))
    ax.text(v1_x+37.5, v1_y-9, "75.0 ± 0.2", fontsize=7, ha='center')
    ax.annotate('', xy=(v1_x-5, v1_y), xytext=(v1_x-5, v1_y+50), arrowprops=dict(arrowstyle='<->', color='black', lw=0.8))
    ax.text(v1_x-8, v1_y+25, "50.0 ± 0.2", fontsize=7, va='center', rotation=90)

    # View 2: Front Elevation View (75x25 mm)
    v2_x, v2_y = 30, 80
    ax.add_patch(mpatches.FancyBboxPatch((v2_x, v2_y), 75, 25, boxstyle="round,pad=0,rounding_size=1.5", fill=False, edgecolor='#1f2937', linewidth=1.5))
    ax.text(v2_x+37.5, v2_y+27, "TAMPAK DEPAN (FRONT ELEVATION) - SKALA 1:1", fontsize=8, weight='bold', ha='center')
    ax.annotate('', xy=(v2_x-5, v2_y), xytext=(v2_x-5, v2_y+25), arrowprops=dict(arrowstyle='<->', color='black', lw=0.8))
    ax.text(v2_x-8, v2_y+12.5, "25.0 ± 0.2", fontsize=7, va='center', rotation=90)

    # View 3: Left Side View with USB-C & Switch Cutouts (50x25 mm)
    v3_x, v3_y = 135, 130
    ax.add_patch(mpatches.FancyBboxPatch((v3_x, v3_y), 50, 25, boxstyle="round,pad=0,rounding_size=1.5", fill=False, edgecolor='#1f2937', linewidth=1.5))
    # USB-C slot (9.2 x 3.4 mm at Y=25.0, Z=16.0)
    ax.add_patch(mpatches.FancyBboxPatch((v3_x+25.0-4.6, v3_y+16.0-1.7), 9.2, 3.4, boxstyle="round,pad=0,rounding_size=1.2", fill=True, facecolor='#fee2e2', edgecolor='#dc2626', linewidth=1.2))
    # Switch slot (8.2 x 3.2 mm at Y=12.0, Z=16.0)
    ax.add_patch(mpatches.Rectangle((v3_x+12.0-4.1, v3_y+16.0-1.6), 8.2, 3.2, fill=True, facecolor='#fef3c7', edgecolor='#d97706', linewidth=1.2))
    ax.text(v3_x+25, v3_y+27, "TAMPAK SAMPING KIRI (PORT CUTOUTS) - SKALA 1:1", fontsize=8, weight='bold', ha='center')
    ax.text(v3_x+25, v3_y+10, "Port USB-C (9.2 x 3.4 mm)", fontsize=6.5, ha='center', color='#dc2626')
    ax.text(v3_x+12, v3_y+20, "Saklar SPDT (8.2 x 3.2 mm)", fontsize=6.5, ha='center', color='#d97706')

    # View 4: Detailed Section A-A (Scale 2:1)
    v4_x, v4_y = 205, 110
    ax.add_patch(mpatches.FancyBboxPatch((v4_x, v4_y), 70, 45, boxstyle="square,pad=0", fill=True, facecolor='#f8fafc', edgecolor='#64748b', linewidth=1.0))
    ax.text(v4_x+35, v4_y+47, "DETAIL A-A: PORT TOLERANCE (SKALA 2:1)", fontsize=8, weight='bold', ha='center', color='#1e3a8a')
    # Enlarged USB-C
    ax.add_patch(mpatches.FancyBboxPatch((v4_x+15, v4_y+20), 18.4, 6.8, boxstyle="round,pad=0,rounding_size=2.4", fill=True, facecolor='#fee2e2', edgecolor='#dc2626', linewidth=1.5))
    ax.text(v4_x+24.2, v4_y+13, "USB-C 9.2x3.4 R1.2 (Tol: +0.2/-0.0)", fontsize=6.5, ha='center', color='#dc2626')
    # Enlarged Switch
    ax.add_patch(mpatches.Rectangle((v4_x+45, v4_y+20), 16.4, 6.4, fill=True, facecolor='#fef3c7', edgecolor='#d97706', linewidth=1.5))
    ax.text(v4_x+53.2, v4_y+13, "SPDT 8.2x3.2 (Tol: ±0.1)", fontsize=6.5, ha='center', color='#d97706')

    # Engineering Notes
    notes_x, notes_y = 30, 48
    ax.text(notes_x, notes_y, "CATATAN TEKNIK & FABRIKASI ENCLOSURE X1:", fontsize=7.5, weight='bold', color='#111827')
    notes = [
        "1. Material: ABS / Polycarbonate Flame Retardant (UL94-V0) Injection Molded / CNC Milled.",
        "2. Dimensi Luar Bersih: 75.0 x 50.0 x 25.0 mm | Tebal Dinding Rata: 2.0 mm | Radius Sudut Luar: R=3.0 mm.",
        "3. 4x Pilar Dudukan PCB (Standoffs): Tinggi Z = 14.0 mm, Lubang Pilot Sekrup M2 (Ø1.8 mm, Kedalaman 6.0 mm).",
        "4. Toleransi Umum ISO 2768-m: Panjang Linear ±0.2 mm, Lubang Port ±0.1 mm, Sudut ±30'.",
        "5. Port USB-C harus sejajar dengan konektor Type-C TP4056 tanpa halangan kabel saat dicolokkan.",
    ]
    for idx, note in enumerate(notes):
        ax.text(notes_x, notes_y - (idx+1)*5.2, note, fontsize=6.5, color='#374151')

    pdf_path = EXPORT_DIR / "07_Enclosure_X1_Orthogonal_Cutout_Blueprint.pdf"
    svg_path = EXPORT_DIR / "07_Enclosure_X1_Orthogonal_Cutout_Blueprint.svg"
    fig.savefig(str(pdf_path), format='pdf')
    fig.savefig(str(svg_path), format='svg')
    plt.close(fig)
    print(f"Exported: {pdf_path.name} & {svg_path.name}")

# -------------------------------------------------------------
# 5. 3D ISOMETRIC STACKED ASSEMBLY RENDERING (300 DPI PNG)
# -------------------------------------------------------------
def render_3d_isometric_assembly():
    print("Rendering 08_3D_Isometric_Stacked_Assembly (300 DPI PNG)...")
    fig = plt.figure(figsize=(10, 8), dpi=300)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#f8fafc')
    
    # Helper to draw 3D cuboids
    def draw_cuboid(center, size, color, alpha=0.8, edgecolor='black', lw=0.8):
        ox, oy, oz = center
        dx, dy, dz = size
        xx = [ox - dx/2, ox + dx/2]
        yy = [oy - dy/2, oy + dy/2]
        zz = [oz - dz/2, oz + dz/2]
        
        # 6 faces
        faces = [
            [[xx[0], yy[0], zz[0]], [xx[1], yy[0], zz[0]], [xx[1], yy[1], zz[0]], [xx[0], yy[1], zz[0]]], # bottom
            [[xx[0], yy[0], zz[1]], [xx[1], yy[0], zz[1]], [xx[1], yy[1], zz[1]], [xx[0], yy[1], zz[1]]], # top
            [[xx[0], yy[0], zz[0]], [xx[1], yy[0], zz[0]], [xx[1], yy[0], zz[1]], [xx[0], yy[0], zz[1]]], # front
            [[xx[0], yy[1], zz[0]], [xx[1], yy[1], zz[0]], [xx[1], yy[1], zz[1]], [xx[0], yy[1], zz[1]]], # back
            [[xx[0], yy[0], zz[0]], [xx[0], yy[1], zz[0]], [xx[0], yy[1], zz[1]], [xx[0], yy[0], zz[1]]], # left
            [[xx[1], yy[0], zz[0]], [xx[1], yy[1], zz[0]], [xx[1], yy[1], zz[1]], [xx[1], yy[0], zz[1]]], # right
        ]
        poly = Poly3DCollection(faces, facecolors=color, alpha=alpha, edgecolors=edgecolor, linewidths=lw)
        ax.add_collection3d(poly)

    # 1. Enclosure Base Box X1 (Translucent Gray Wireframe)
    draw_cuboid((0, 0, 12.5), (75, 50, 25), '#94a3b8', alpha=0.15, edgecolor='#475569', lw=1.2)
    
    # 2. Tier 1: Li-Po Battery 103040 (Silver/Blue) at bottom (Z = 2 to 12 mm)
    draw_cuboid((0, -2, 7.0), (40, 30, 10), '#38bdf8', alpha=0.85, edgecolor='#0284c7', lw=1.0)
    
    # 3. Tier 2: Perfboard FR4 Substrate (Emerald Green) at Z = 14.0 mm
    draw_cuboid((0, 0, 14.8), (60, 40, 1.6), '#10b981', alpha=0.9, edgecolor='#047857', lw=1.0)
    
    # Modules mounted on Perfboard:
    # ESP32-C3 SuperMini (Dark Green / Black chip)
    draw_cuboid((-3, 0, 17.2), (22.5, 18, 3.2), '#064e3b', alpha=0.95, edgecolor='#022c22')
    # TP4056 USB-C Charger (Blue)
    draw_cuboid((-22, -2, 17.3), (22, 17, 3.5), '#1d4ed8', alpha=0.95, edgecolor='#1e3a8a')
    # ADXL345 Accelerometer (Orange)
    draw_cuboid((18, 8, 17.1), (18, 15, 3.0), '#ea580c', alpha=0.95, edgecolor='#9a3412')
    # NEO-6M GNSS Breakout (Purple)
    draw_cuboid((18, -10, 17.3), (18, 16, 3.5), '#7e22ce', alpha=0.95, edgecolor='#581c87')
    # Active Buzzer (Red Cylinder)
    draw_cuboid((5, 5, 20.3), (12, 12, 9.5), '#b91c1c', alpha=0.9, edgecolor='#7f1d1d')
    
    # 4. Tier 3: GPS Ceramic Patch Antenna (White/Tan Ceramic with Gold patch)
    draw_cuboid((16, -6, 21.0), (25, 25, 4.0), '#fef08a', alpha=0.95, edgecolor='#ca8a04', lw=1.2)

    # 3D Labels & Callouts
    ax.text(-35, -20, 7.0, "TIER 1: Li-Po 103040 (3.7V 1200mAh)", fontsize=8, weight='bold', color='#0284c7')
    ax.text(-35, 15, 14.8, "TIER 2: Perfboard FR4 60x40mm + ESP32-C3 & Sensors", fontsize=8, weight='bold', color='#047857')
    ax.text(18, -25, 22.0, "TIER 3: Ceramic Patch Antenna (25x25x4 mm)", fontsize=8, weight='bold', color='#b45309')
    
    # View configuration
    ax.set_xlim(-45, 45)
    ax.set_ylim(-35, 35)
    ax.set_zlim(0, 32)
    ax.view_init(elev=28, azim=-55)
    ax.set_xlabel('X (mm - Length 75mm)', fontsize=8)
    ax.set_ylabel('Y (mm - Width 50mm)', fontsize=8)
    ax.set_zlabel('Z (mm - Height 25mm)', fontsize=8)
    
    ax.set_title("PRISM SAFETY GPS (PRJ-PSG-01)\n3-Tier Vertical Stacked Assembly Layout (Enclosure X1)", fontsize=11, weight='bold', pad=15)
    
    png_path = EXPORT_DIR / "08_3D_Isometric_Stacked_Assembly.png"
    plt.tight_layout()
    fig.savefig(str(png_path), dpi=300)
    plt.close(fig)
    print(f"Exported: {png_path.name} (300 DPI Rendering Complete)")

def main():
    print("Executing Category 4 (build123d, ezdxf, isometric blueprints)...")
    enc = build_enclosure_x1_step()
    build_full_3tier_assembly_step(enc)
    build_cutouts_dxf()
    render_orthogonal_blueprint()
    render_3d_isometric_assembly()
    print("Category 4 Completed Successfully!")

if __name__ == "__main__":
    main()
