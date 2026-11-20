import subprocess
from pathlib import Path

kicad_cli = r"C:\Program Files\KiCad\10.0\bin\kicad-cli.exe"
root_sch = Path(r"C:\Antigravity\PRISM SAFETY GPS\cad_eda\02_KiCad_Schematic_PCB\PRISM_SAFETY_GPS.kicad_sch")
test_file = Path(r"C:\Antigravity\PRISM SAFETY GPS\cad_eda\02_KiCad_Schematic_PCB\test.kicad_sch")

text = root_sch.read_text(encoding="utf-8")

def parse_sexpr(s):
    tokens = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == '(':
            start = i
            depth = 1
            i += 1
            in_str = False
            while i < n and depth > 0:
                if s[i] == '"' and s[i-1] != '\\':
                    in_str = not in_str
                elif not in_str:
                    if s[i] == '(':
                        depth += 1
                    elif s[i] == ')':
                        depth -= 1
                i += 1
            tokens.append(s[start:i])
        else:
            i += 1
    return tokens

outer = text.strip()
inner = outer[len("(kicad_sch"): -1]
children = parse_sexpr(inner)

def check_range(k):
    test_content = "(kicad_sch\n" + "\n".join(children[:k]) + "\n)"
    test_file.write_text(test_content, encoding="utf-8")
    r = subprocess.run([kicad_cli, "sch", "erc", str(test_file)], capture_output=True, text=True)
    return r.returncode != 3

low = 1
high = len(children)
print(f"Binary searching between 1 and {high}...")

while low < high:
    mid = (low + high) // 2
    ok = check_range(mid)
    print(f"Checking prefix {mid}: {'OK' if ok else 'FAIL'}", flush=True)
    if ok:
        low = mid + 1
    else:
        high = mid

print(f"First failing child is {low - 1}:")
print(children[low - 1][:200])
