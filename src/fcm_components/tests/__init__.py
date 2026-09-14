# SPDX-License-Identifier: BSD-3-Clause
"""Unit tests for fcm-components — one module per component.

``test_<component>.py`` covers the component in ``<component>.py``, against the
cases in ``docs/test-plans/<component>.md``. The three names match, so any one
of them finds the other two.

Run the lot, or one component's:

    python runtests.py
    python runtests.py fcm_components.tests.test_package

The ``test_`` prefix is not decoration — Django's runner discovers modules
matching ``test*.py``, so a module named for the component alone is collected
by nothing and passes by never running.
"""
