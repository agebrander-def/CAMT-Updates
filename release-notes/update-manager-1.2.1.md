# CAMT Update Manager 1.2.1 — Network Resilience

## Changes
- Uses `requests` as primary HTTPS client.
- Keeps `urllib` as independent fallback.
- Retries transient connection resets/time-outs up to three rounds with short back-off.
- HTTP 4xx errors that are not transient fail immediately.
- Caches the last valid `update.json` and `modules.json`.
- When GitHub is temporarily unreachable, cached valid update data can remain available.
- Downloads are first written to `.part` and moved into place only after a complete transfer.
- Temporary network failures are shown as a normal CAMT message instead of raw `urlopen` / `WinError 10054` exception text.
- SHA-256 and optional Ed25519 validation remain in place.

No CAMT.exe/PyInstaller rebuild is required for this module update.
