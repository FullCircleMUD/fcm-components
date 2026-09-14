# CLAUDE.md

> **Project-wide working rules and cross-repo context live in the FCM umbrella repo's `CLAUDE.md`**,
> loaded automatically when you work from the umbrella root. If you opened this repo directly instead
> of via the umbrella, relaunch from the umbrella root for the full context. This file holds only this
> repo's specific instructions.

Instructions for Claude (and other LLM agents) working in this repository.

## What this project is

`fcm-components` holds the pieces of FullCircleMUD that are worth separating but too small to be a
library of their own — a mixin, a helper, a component with an important job and few moving parts. Each
one is a module with its own interface and its own consumers. Tagline: **"FCM's shared components —
one module per component, for Evennia games."**

For the big-picture overview, read [README.md](README.md).
For the design wiki, read [docs/INDEX.md](docs/INDEX.md).

## Project status

For the current state — what has been extracted, what is pending — see
[docs/progress.md](docs/progress.md), the running log of milestones with links to evidence.

Nothing has been extracted into the library yet. The repository is scaffolded and no more.

## Where to read first

For any non-trivial task, start by reading in this order:

1. [README.md](README.md) — what the project is, status, quick start.
2. [docs/test-plans/INDEX.md](docs/test-plans/INDEX.md) — where a behavioural change starts. A case
   lands in its component's plan before the test, and the test before the code.
3. [docs/INDEX.md](docs/INDEX.md) — map of all design docs.

## Load-bearing architectural principles

These are the principles every implementation decision must respect. Getting them wrong is expensive to
undo.

1. **This is an FCM library, and FCM concepts belong in it.** The `fcm-` prefix is the whole point of
   the name. Every `evennia-*` sibling carries "the library does not own game concepts" and "no
   FCM-specific assumptions" as principles; **this library carries neither**, and adding them back
   would be a mistake. The components here are FCM's, and the library makes no claim to drop into an
   arbitrary Evennia install.

   That is not licence to be careless — scope calls still get made, case by case, as concrete
   questions arise. It removes the blanket rule, not the judgement.

2. **One component, one module — and one test plan, and one test package.** The unit that gets
   refactored here is the component, not the library. That is what makes the library's grab-bag shape
   workable: a change to one component has consumers you can name, where "who consumes
   fcm-components" would answer "everything" and say nothing.

   Everything is organised on that boundary, not just the code:

   - **Code** — `src/fcm_components/<component>.py`
   - **Tests** — `src/fcm_components/tests/test_<component>.py`
   - **Test plan** — `docs/test-plans/<component>.md`

   **The three names match**, so any one of them finds the other two. One file each: components are
   small enough that splitting further would cost more than it finds.

   **Each component's tests must be runnable on their own**, without the rest of the suite:

   ```
   python runtests.py fcm_components.tests.test_<component>
   ```

   That is a requirement on how tests are written, not just how files are named — a case that only
   passes because another component's module ran first has coupled two components through the suite.

   Two things follow from the whole arrangement. A reader asking what one component promises opens
   one file. And promotion out into its own library moves three files rather than carving sections
   out of shared ones.

3. **Modules do not reach across without a declaration.** A component may depend on another component
   in this library, but never silently. The dependency is declared where a reader will find it, so the
   set of couplings inside the library is enumerable rather than discovered later when something will
   not come loose.

   `[TBD — needs discussion: what enforces this. A declaration in the module header checked by the
   library-standards-linter was proposed; nothing is agreed. Until then it is a convention.]`

4. **A component is a library that has not proved it needs to be one.** Where it is unclear whether
   something warrants its own repository, it is built here first. The building is the thinking work,
   and the answer arrives with evidence behind it. A component that outgrows the slot is promoted out
   into its own library rather than left here.

   `[TBD — needs discussion: what signals promotion, and what the promotion actually involves.]`

5. **Test-first.** A case lands in the component's plan under
   [docs/test-plans/](docs/test-plans/INDEX.md), then the test, then the code. See
   [test-first-process.md](../../design/test-first-process.md) for the process and the rationale.

## Out of scope

Scope boundaries are decided as concrete questions arise, by applying the principles above. Nothing is
ruled out yet — there is no code to rule on.

## Working conventions

- **Editing design docs.** Update or add design documents whenever an architectural decision is made or
  refined. Capture the *why*, not just the *what*. Index new docs in [docs/INDEX.md](docs/INDEX.md).
- **A component's own constants live in the component's module — a deliberate divergence.** The
  library standard puts every module-level constant in `config.py`. Here that would cut every
  component in half and make promotion a merge rather than a file move, which is principle 2 lost for
  a discovery benefit the per-component boundary already provides. `DIRECTIONS` and `BUILD_REFUSED`
  live in `compass_navigation.py`, and the `constant_outside_config` warning against them is this
  decision rather than a gap. **Do not "fix" it.**

  A constant genuinely shared *between* components is the case `config.py` exists for, and it lands
  there. The file does not exist yet.
- **Licensing — BSD-3-Clause, deliberately unlike the other `fcm-*` repositories.** `fcm-xrpl` and
  `fcm-subscriptions` are unlicensed and proprietary because the on-chain layer and the payment flow
  are where FCM's competitive edge sits. Nothing in this library is: how exits are defined and how room
  classes are put together is largely standard Evennia work with integration points. So there is a
  `LICENSE` file, source files carry `# SPDX-License-Identifier: BSD-3-Clause` on the first line, and
  `pyproject.toml` declares `BSD-3-Clause`.

  **Do not "fix" this to match the sibling `fcm-*` repositories.** The difference is the decision, not
  an oversight. It is the current position and open to revision like anything else — if something
  genuinely sensitive lands here, that is the conversation to have.
- **Test plans are per component — a deliberate divergence from the library standards.** The standard
  and its `library-standards-linter` both expect one `docs/test-plan.md` per library, so this
  repository carries a standing `missing_file` warning until the standard is taught the folder form.
  That warning is this decision, not a gap — do not "fix" it by adding a library-wide plan. The
  divergence is principle 2 applied: a library whose unit is the component cannot hold its
  commitments in one file without losing the boundary it exists for.

  `[TBD — needs discussion: whether `design/library-standards.md` and the linter learn the folder
  form, or this stays a recorded per-library divergence.]`
- **Don't put implementation detail in this file or README.** Link out to docs/ instead. Keep CLAUDE.md
  and README.md stable; let docs/ churn.

## Documentation discipline (load-bearing)

Design documents in `docs/` must reflect decisions **actually discussed and agreed on with the project
owner**. They are not a place to forward-design the system from first principles or extrapolate
"reasonable defaults" from a starting point.

**Rules:**

1. **Only capture what was discussed and agreed.** If the conversation establishes a principle, do not
   extrapolate it into specifics that were not raised.
2. **Flag open questions explicitly.** Where a topic has been raised but not resolved, write
   `[TBD — needs discussion: <what is open>]` in the doc. Future sessions then pick the topic up
   deliberately rather than inheriting unagreed assumptions.
3. **Distinguish archived material from in-conversation decisions.** Material in `docs/archive/` is
   preserved historical context, not authoritative. Restating it in new docs is acceptable when it
   provides necessary context, but mark it as such.
4. **Smaller is better.** A doc that captures three discussed points faithfully is more useful than one
   that captures three discussed points plus seven invented ones. Resist the urge to fill out sections
   "for completeness."

If a session catches itself writing content that goes beyond what was discussed, stop and either remove
the extrapolation or convert it to a `[TBD]` marker.

## Repository layout

```
fcm-components/
├── CLAUDE.md                  # this file
├── README.md
├── LICENSE                    # BSD 3-Clause
├── pyproject.toml
├── runtests.py                # standalone test runner; no gamedir required
├── .gitignore
├── docs/                      # technical wiki (humans + LLMs)
│   ├── INDEX.md
│   ├── installing.md          # the numbered steps a consumer works down
│   ├── progress.md
│   ├── test-plans/            # one plan per component, not one per library
│   │   ├── INDEX.md
│   │   └── package.md         # the library package itself; SM cases
│   ├── interoperability.md
│   └── archive/               # historical context (currently empty)
├── src/
│   └── fcm_components/        # library code (src layout)
│       ├── __init__.py
│       ├── log.py             # components_log — the make_logger binding
│       └── tests/             # one test module per component
│           ├── __init__.py
│           └── test_package.py
└── tests/                     # standalone test infrastructure
    ├── __init__.py
    ├── test_settings.py
    └── urls.py
```

No component modules yet. No `config.py` — it lands with the first constant. No `examples/` — it lands
when there is a surface worth driving from a live gamedir.

## Tools and environment

- Python 3.10+ (pinned via `pyproject.toml`).
- Runtime dependencies: `evennia`, `evennia-logging-extension`. The extension is not on PyPI —
  editable-install it from its checkout into any venv that runs this one, before `pip install -e .`.
- **Tests use Django's test runner** via `runtests.py`, which bootstraps Django then calls
  `evennia._init()`, as the siblings do. No gamedir required.
- Dedicated venv at `fcm-components/venv/` (gitignored). Development install via `pip install -e .`.

## Sibling libraries to reference

When in doubt about a convention not covered here, look at how a sibling library does it:

- **[../fcm-subscriptions/](../fcm-subscriptions/)** — the closest structural model: the same `fcm-`
  family, the same `runtests.py` and test-settings shape, the same nine-section `CLAUDE.md`.
