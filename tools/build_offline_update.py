import argparse,json,zipfile
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument("installer");ap.add_argument("--output",required=True);a=ap.parse_args()
m=json.loads(Path("update.json").read_text(encoding="utf-8"));p=Path(a.installer);m["offline_asset"]=p.name
with zipfile.ZipFile(a.output,"w",zipfile.ZIP_DEFLATED) as z:
 z.writestr("update.json",json.dumps(m,indent=2,ensure_ascii=False));z.write(p,p.name)
print(a.output)
