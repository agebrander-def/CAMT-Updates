import argparse,base64,hashlib,json
from pathlib import Path

def canonical(m):
    d=json.loads(json.dumps(m));d.setdefault("signing",{})["signature"]="";return json.dumps(d,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()

ap=argparse.ArgumentParser();ap.add_argument("installer");ap.add_argument("--version",required=True);ap.add_argument("--build",required=True);ap.add_argument("--download-url",required=True);ap.add_argument("--channel",default="Beta");ap.add_argument("--release-seq",type=int,required=True);ap.add_argument("--private-key");ap.add_argument("--notes",default="");a=ap.parse_args()
p=Path(a.installer);m=json.loads(Path("update.json").read_text(encoding="utf-8"))
m.update({"version":a.version,"build":a.build,"channel":a.channel,"release_seq":a.release_seq,"download_url":a.download_url,"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"release_notes":a.notes})
m.setdefault("signing",{}).update({"algorithm":"ed25519","signature":""})
if a.private_key:
    from cryptography.hazmat.primitives import serialization
    key=serialization.load_pem_private_key(Path(a.private_key).read_bytes(),password=None)
    m["signing"]["signature"]=base64.b64encode(key.sign(canonical(m))).decode()
Path("update.json").write_text(json.dumps(m,indent=2,ensure_ascii=False),encoding="utf-8")
print("Updated update.json")
print("SHA-256:",m["sha256"])
print("Signed:",bool(m["signing"]["signature"]))
