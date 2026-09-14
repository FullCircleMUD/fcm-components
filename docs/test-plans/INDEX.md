# Test plans

One plan per component, not one for the library. A reader asking "what does this component promise?"
opens one file and finds all of it; a component promoted out into its own library takes its plan with
it as a file rather than as a section someone has to carve out.

A case lands in its component's plan **before** the test, and the test before the code — see
[test-first-process.md](../../../../design/test-first-process.md).

## Conventions

- **Three files per component, and the names match**, so any one of them finds the other two:

  | | |
  |---|---|
  | Code | `src/fcm_components/<component>.py` |
  | Tests | `src/fcm_components/tests/test_<component>.py` |
  | Plan | `docs/test-plans/<component>.md` |

- **A component's tests run on their own**: `python runtests.py fcm_components.tests.test_<component>`.
  A case that only passes because another component's module ran first has coupled two components
  through the suite, and is a defect in the case.
- **Case ID prefixes are unique across the library.** The plans are separate files but the IDs share
  one namespace, so a case ID in a commit message or a test docstring identifies one case without
  naming its file. IDs are never renumbered — retire one rather than reuse it.
- **Each plan carries its own fixtures table**, covering what its own cases need. A fixture two
  components both need is a sign one of them should be depending on the other — see principle 3 in
  [CLAUDE.md](../../CLAUDE.md).
- **A case carrying `[TBD]` does not pass** — unresolved behaviour is an error until the decision is
  made.

## Plans

| Plan | Prefix | Tests | Covers |
|---|---|---|---|
| [package.md](package.md) | `SM` | `tests/test_package.py` | The library package itself — install and test runner. Not a component |

*(No component plans yet. Each one lands here as its component is agreed, before any of its code is
written.)*
