# Residency and Audit

A new data residency rule from Legal reaches a dozen places across three documents. The AI finds them, redraws the diagrams, and then audits its own work.

**Length:** About 20 minutes. **Use it for:** A full slot where you want the strongest proof that nothing is missed.

Northwind Outfitters and everything about its Sales Insights Platform is fictional.

## Start here

Open the [presenter guide](presenter-guide.md). It lists what to set up, what to show, and what to paste at each step.

## Contents

- [presenter-guide.md](presenter-guide.md): The step-by-step run, with every prompt, an answer key, and the reset step.
- [project/](project/README.md): The folder you give the AI. It holds the documents and the rules the AI follows, and nothing about the demo itself.
- [before/](before/README.md): A frozen Word document and PNG that show the old way.
- [demo-010-residency-and-audit-before-after.png](demo-010-residency-and-audit-before-after.png): Visual before-and-after walkthrough of the demo run.

## Run it

```bash
git switch -c demo-run
```

Open your AI tool in the `project/` folder, then follow the presenter guide. The folder carries its own `AGENTS.md`. If your tool does not read it automatically, start with "Read AGENTS.md and follow it." Reset afterwards:

```bash
git switch main && git branch -D demo-run
```

**Navigation:** [Demo index](../README.md) · [Repository home](../../README.md)
