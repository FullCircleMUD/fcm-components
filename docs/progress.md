# Progress

Running log of milestones with links to evidence. Reverse chronological — newest first.

## 2026-09-14 — repository scaffolded (latest)

- **Structure only.** `pyproject.toml`, the `src/fcm_components/` package with its `__init__.py` and
  `log.py`, `runtests.py` and the `tests/` scaffolding, the five `docs/` surfaces and `CLAUDE.md`. No
  component has been extracted.

- **One smoke test**, `SM-01` — the package imports and reports a version. It proves the install and
  the runner reach the package, and nothing about behaviour.

- **BSD-3-Clause**, unlike the two sibling `fcm-*` repositories. They are proprietary because the
  on-chain layer and the payment flow are where the competitive edge sits; nothing expected to land
  here is. Recorded in [CLAUDE.md](../CLAUDE.md) under *Working conventions* so it is not "fixed" to
  match them.

- **Test plans are per component**, in [test-plans/](test-plans/INDEX.md) rather than one
  `test-plan.md`. Principle 2 applied to the documentation: the unit here is the component, so a
  component's commitments live in one file it can be promoted out with. The library standards expect
  the single-file form, so the linter carries a standing warning against this library until that is
  settled. `0 error, 3 warn` is the clean state here.

- **Three files per component, names matching** — `<component>.py`, `tests/test_<component>.py`,
  `test-plans/<component>.md`. Each component's tests run on their own; verified against the smoke
  case both ways, `python runtests.py` and `python runtests.py fcm_components.tests.test_package`.

- **Open questions**, each recorded as `[TBD]` where it belongs: what enforces the
  no-silent-cross-module-dependency rule, what signals promotion out into a library, and whether the
  library standards learn the test-plans folder form.
