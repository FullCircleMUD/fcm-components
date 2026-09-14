# SPDX-License-Identifier: BSD-3-Clause
"""The library package itself: that it installs and the runner reaches it.

Cases: docs/test-plans/package.md. Not a component — this one covers the
container, and it stays when every component has been promoted out.
"""

import unittest


class SmokeTest(unittest.TestCase):
    """SM — smoke: install and runner."""

    def test_the_package_reports_a_version(self):
        """SM-01 — the package imports and carries a ``__version__``."""
        import fcm_components

        self.assertTrue(fcm_components.__version__)
