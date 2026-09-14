# Test plan — the package

The library package itself: that it installs, and that the test runner reaches it. This is the one
plan that is not a component's — it covers the container, and it stays here when every component has
been promoted out.

Tests: `src/fcm_components/tests/test_package.py`, runnable on their own with
`python runtests.py fcm_components.tests.test_package`.

An empty `Test function` cell is agreed behaviour not yet covered; that column is the coverage trail,
and it is checked both ways.

## Fixtures

| Fixture | Purpose |
|---|---|

*(None. The smoke case needs no fixtures.)*

## SM — smoke: install and runner

| ID | Case | Test function |
|---|---|---|
| SM-01 | The package imports and carries a `__version__` | `SmokeTest.test_the_package_reports_a_version` |

## Open decisions

*(None.)*
