# CLAUDE.md

Guidance for AI assistants (Claude Code and others) working in this repository.

## Repository status

This repository is currently a **blank slate**. As of the latest commit it
contains only:

```
.
├── README.md   # single-line title ("# Claude")
└── CLAUDE.md   # this file
```

There is no application source code, build system, dependency manifest,
test suite, or CI configuration yet. The sections below describe the
conventions already in force and act as a template to fill in as the
project takes shape.

> **Keep this file current.** When real code lands, update CLAUDE.md in the
> same change: document the actual structure, the commands to build/test/lint,
> and any conventions you establish. Treat an out-of-date CLAUDE.md as a bug.

## Repository facts

- **Remote / project:** `diyaidev/Claude`
- **Default branch:** `main`
- **Language / stack:** not yet established

## Git workflow & conventions

- **Do not commit directly to `main`.** Develop on a feature branch and open
  a pull request for review.
- **Branch naming:** feature branches in this project follow the
  `claude/<short-description>-<id>` pattern (e.g. `claude/claude-md-docs-kh9ijv`).
  Create the branch locally if it does not already exist.
- **Commits:** write clear, descriptive, imperative-mood messages
  (e.g. "Add CLAUDE.md with repo conventions"). Keep each commit focused.
- **Pushing:** push with `git push -u origin <branch-name>`. On transient
  network failures, retry with exponential backoff.
- **Pull requests:** only open a PR when explicitly asked. If a PR template
  exists under `.github/`, mirror its structure when filling out the body.

## How to extend this document

When you add the first real components, replace the placeholders below with
concrete, verified instructions:

- **Project overview** — what the project does and its high-level architecture.
- **Directory structure** — the meaningful top-level directories and their roles.
- **Setup** — how to install dependencies and prepare a dev environment.
- **Build / run** — the exact commands to build and run the project locally.
- **Test** — how to run the test suite (and how to run a single test).
- **Lint / format** — the linters/formatters and how to invoke them.
- **Conventions** — naming, code style, error handling, and module patterns
  that aren't obvious from a single file.
- **Gotchas** — anything non-obvious that would trip up a new contributor.

Only document commands and conventions you have actually verified in the
repository — do not invent tooling that isn't present.
