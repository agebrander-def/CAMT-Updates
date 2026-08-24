CAMT MODULE UPDATE TEST

1. Import CAMT_Update_Manager_v1_1_0.camtmodule once through CAMT Module Manager.
2. Upload the CONTENTS of this repository kit to https://github.com/agebrander-def/CAMT-Updates on branch main:
   - modules.json in repository root
   - modules/CAMT_Update_Manager_v1_1_1.camtmodule
   - release-notes/update-manager-1.1.1.md
3. Open CAMT Update Manager v1.1.0.
4. Click Module-updates.
5. It should show 1.1.0 -> 1.1.1.
6. Select it and click Geselecteerde module bijwerken.
7. SHA-256 and package identity/version are verified, then Framework 2.0 replaces only the module.
8. Close/reopen CAMT Update Manager. It should now be v1.1.1.

No CAMT.exe or Inno installer download is involved in this module-only test.
