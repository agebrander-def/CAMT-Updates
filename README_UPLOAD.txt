CAMT MODULE REPOSITORY 1.2 - GITHUB UPLOAD

Repository:
https://github.com/agebrander-def/CAMT-Updates

Upload/replace the CONTENTS of this kit in the repository root:

modules.json
modules/
release-notes/

IMPORTANT
The supplied modules.json deliberately still uses schema CAMT.ModuleUpdateCatalog.1.
That lets an already installed CAMT Update Manager 1.1.1 see and install its own 1.2.0 update.
After 1.2.0 is loaded, the same catalog is treated as a full Module Repository and the three modules that are not installed appear under Available.

TEST FLOW
1. Upload this kit and commit to main.
2. In existing Update Manager 1.1.1: Module updates -> Check modules.
3. Update CAMT Update Manager 1.1.1 -> 1.2.0.
4. Close and reopen CAMT Update Manager.
5. Open Module Repository.
6. The three new modules should appear under Available even when no base version is installed.
7. Install one or more directly from the repository.

No PyInstaller or CAMT.exe rebuild is required.
