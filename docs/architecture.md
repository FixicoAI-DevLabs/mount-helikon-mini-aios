# Mini architecture

Mini is a free, open-source starter using two runtime layers. **System** is account Personalization: two snippets in Custom instructions and More about you. **Operating** is the exact compact JSON saved in the account Library. Ordinary non-project chats are the primary product surface; Projects are optional.

## Preserve the Mini setup, replace the old runtime

| Mini 3.3 setup | Mini 4.1 implementation |
|---|---|
| Account-wide Personalization | Preserved as two separate snippets, each at most 1,500 characters |
| Ordinary-chat guided installation | Preserved through SETUP / INSTALL / NEXT / FINAL_VERIFY |
| One authoritative install package | Restored; embeds exact snippets, runtime bytes and installer protocol |
| Six Saved Memories as Operating | Replaced with one runtime-only JSON derived from Helikon 6 |
| Optional Projects | Preserved as optional organization or explicit alternate delivery |
| Eight-file end-user bundle | Restored; developer tooling and tests stay in the repository |
| Universal approval tokens / footer conventions | Replaced with scoped authorization and exact-format compliance from Helikon 6 |

The project-only 4.0 release did not preserve the required installation model. Its artifacts and evidence remain historical; 4.1 changes the System delivery contract and requires new account-level verification.

## Build sources and generated outputs

Maintainer sources are `installer/custom_instructions.txt`, `installer/more_about_you.txt`, `installer/contract.json` and the root runtime JSON. `tools/installer.py` generates the unified install package and the two-snippet Markdown sheet. `tools/mini.py render` also regenerates the human-readable Operating reference. Validation rejects drift between sources and shipped projections.

The install package is the installation authority distributed to end users. Once installed, only the standalone JSON is designated Operating. Installer instructions, personal backups, source bindings, test records and release history stay outside the runtime.

All twelve logical Helikon owners and the reviewed compact runtime rules remain. Runtime policy text is unchanged from 4.0; the repaired candidate uses runtime 4.1.1-candidate.1, schema 1.0.7 and System contract 2.1.0. The two-field System and delivery protocol have changed substantively, so earlier project behavior evidence cannot establish their account-wide behavior. The schema patch pins the new identity and corrects its descriptive title; it does not add runtime structures.

The candidate shortens the account snippets, clarifies full-source reading before Mini-dependent work, and moves the fresh-chat handoff into complete copyable instructions. Installer protocol 2.1.0 and installation record 2.0.0 are independently versioned. These changes require new live observations; offline consistency does not establish account operation.

## Source and authority boundaries

Read the complete selected runtime through real available tools, verify all four identity pairs and refresh missing exact text. A filename, checksum, marker, summary or self-report is insufficient. Library search availability is not a guarantee of per-chat full content delivery. Missing access must be disclosed, with manual Add from Library identified as a fallback.

Mini remains user-level guidance under host instructions. It cannot create tools, grant permissions or prove effects. Current scoped authorization carries forward; no universal approval token, mandatory footer, Saved Memory installation or optional Skill is required. Exact-format tasks must not acquire configuration commentary.
