# Tools

The folder holds scripts that keep this repository's documentation correct.

## Contents

- [check-docs.py](check-docs.py): Confirms every relative link resolves and every `mermaid` and `d2` block renders.
- [test-check-docs.py](test-check-docs.py): Tests that the checker fails on a broken link, a broken Mermaid block, and a broken D2 block.

## Run it

```bash
python3 tools/check-docs.py
```

- **Mermaid blocks:**
  - Render locally when `mmdc` (Mermaid CLI) is installed.
  - Are skipped with a notice when `mmdc` is missing.
- **D2 blocks:**
  - Render through the service named in the `D2_RENDERER_URL` environment variable, for example a self-hosted D2 render endpoint that accepts D2 text at `/d2/svg`.
  - Fall back to the local `d2` command, with the ELK layout, when the variable is not set.
  - Are skipped with a notice when neither is available.

## Test the checker

```bash
python3 tools/test-check-docs.py
```

Diagram cases skip when no renderer is available. [TESTING.md](../TESTING.md) explains what each check protects.

**Navigation:** [Repository home](../README.md)
