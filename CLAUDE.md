# Claude Instructions — halo-terra-presets

> **IMPORTANT: Read [CONTEXT.md](CONTEXT.md) before doing anything in this project.**

CONTEXT.md is kept current by automation (see "How CONTEXT.md is Updated" below)
and contains the authoritative, up-to-date snapshot of this codebase. Always read
it first so you understand:

- Current architecture and module map
- Active TODOs and known constraints
- Tech stack, key dependencies, and environment variables
- Recent changes (last 10 commits)

---

## Quick Start

```bash
# Install dependencies
# No dependencies -- generate_presets.py uses only the Python standard library (os, uuid)

# Run tests
# no test suite -- this is a static preset/asset library

# Run the application
python generate_presets.py
```

---

## Project-Specific Constraints

<!-- Add permanent constraints, invariants, or non-obvious rules here.
     This section is NOT auto-generated and will not be overwritten.

     Examples:
     - Safety invariants (e.g., "dry-run by default — never mutate without --confirm")
     - Frozen thresholds (e.g., "confidence threshold is 0.85 — do not change without data")
     - External dependencies (e.g., "requires Gmail OAuth credentials in .env")
     - Code style decisions (e.g., "no type stubs for internal modules")
-->

---

## How CONTEXT.md is Updated

CONTEXT.md is regenerated automatically:
- On pushes to `main`/`master` (except commits that only touch `CONTEXT.md` itself)
- On every pull request
- Daily at 03:00 UTC

To regenerate manually:
```bash
python scripts/generate_context.py
```

To validate quality:
```bash
python scripts/validate_context.py
```

---

_This CLAUDE.md was installed by [claude-context-sync](https://github.com/thead4md/claude-context-sync)._
