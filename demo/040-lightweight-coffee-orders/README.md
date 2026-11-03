# Lightweight Coffee Orders

Two short documents, one Mermaid diagram and one D2 diagram. Executives ask questions about them, then one sentence adds mobile pre-orders, and the new boxes appear outlined in green, so the audience sees what changed without reading a diagram.

**Length:** About 6 minutes. **Use it for:** A very short slot, a first demo for a new audience, or a second demo after the [crash course](../../education/005-crash-course.md). It is also the safest demo when you present with a small or fast AI model, because the diagrams are tiny.

Bramble Coffee and everything about it is fictional.

## Start here

Open the [presenter guide](presenter-guide.md). It lists what to set up, what to paste, and what to show.

## Contents

- [presenter-guide.md](presenter-guide.md): The step-by-step run, with every prompt, an answer key, and the reset step.
- [project/](project/README.md): The folder you give the AI. It holds the two documents and the rules the AI follows, and nothing about the demo itself.
- [demo-040-lightweight-coffee-orders-before-after.png](demo-040-lightweight-coffee-orders-before-after.png): Visual before-and-after walkthrough of the demo run.

## Run it

```bash
git switch -c demo-run
```

Open your AI tool in the `project/` folder, then follow the presenter guide. The folder carries its own `AGENTS.md`. If your tool does not read it automatically, start with "Read AGENTS.md and follow it." Reset afterwards:

```bash
git switch main && git branch -D demo-run
```

**Navigation:** [Demo index](../README.md) · [Repository home](../../README.md)
