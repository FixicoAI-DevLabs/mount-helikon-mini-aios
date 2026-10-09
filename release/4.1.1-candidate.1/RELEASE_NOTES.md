# Helikon Mini 4.1.1-candidate.1 — repository repairs

Status: **review/testing candidate; live account acceptance not run**. This is a separate candidate artifact, not a replacement for the preserved 4.1.0 testing bundle or the regular 4.0 project release.

The candidate repairs exact-byte handling and evidence preservation, shortens the Personalization snippets to 1,100 and 867 characters, and makes the fresh ordinary-chat handoff self-contained. It adds structured installation records, historical/current manifest checks, source-inventory checks and an expanded manual acceptance suite.

The compact runtime's rules, procedures, bootstrap, owners and extension declarations are unchanged. Its identity is advanced to runtime 4.1.1-candidate.1, schema 1.0.7 and System contract 2.1.0; the extension contract remains 1.0.0. The System instructions and installer protocol changed and require fresh host testing. Install-package schema and installer protocol are 2.1.0; installation-record schema is 2.0.0.

Use the candidate bundle's START_HERE.md for review or an appropriately scoped test installation. Preserve existing settings and active full Helikon. The package does not change an account by itself. Do not attach either the runtime or install package to the primary automatic Library-access test.

See [executed offline validation](VALIDATION.md), [repair disposition](REPAIR_MAP.md), and the [manual acceptance suite](../../docs/account-acceptance.md). Historical project pilots and full Helikon 6 installation observations do not pass these account gates. No general usefulness advantage is claimed.
