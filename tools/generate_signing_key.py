from pathlib import Path
try:
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    from cryptography.hazmat.primitives import serialization
except ImportError:
    raise SystemExit("Install cryptography first: python -m pip install cryptography")
priv=Ed25519PrivateKey.generate();pub=priv.public_key()
Path("CAMT_UPDATE_PRIVATE_KEY.pem").write_bytes(priv.private_bytes(serialization.Encoding.PEM,serialization.PrivateFormat.PKCS8,serialization.NoEncryption()))
Path("CAMT_UPDATE_PUBLIC_KEY.pem").write_bytes(pub.public_bytes(serialization.Encoding.PEM,serialization.PublicFormat.SubjectPublicKeyInfo))
print("Created CAMT_UPDATE_PRIVATE_KEY.pem and CAMT_UPDATE_PUBLIC_KEY.pem")
print("KEEP THE PRIVATE KEY OFF GITHUB.")
