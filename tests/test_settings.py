# SPDX-License-Identifier: BSD-3-Clause
"""Minimal Django settings for fcm-components unit tests.

Imports Evennia's defaults, adds the library to INSTALLED_APPS, and runs an
in-memory sqlite database. No gamedir required.
"""

import os
import sys
import tempfile

import evennia

# Evennia 6.0.0+ ships migrations that import ``typeclasses.objects``
# (a gamedir module). Put Evennia's game_template on sys.path so the
# import resolves without requiring a real gamedir.
_game_template = os.path.join(os.path.dirname(evennia.__file__), "game_template")
if _game_template not in sys.path:
    sys.path.insert(0, _game_template)

from evennia.settings_default import *  # noqa: F401, F403, E402

# Evennia path bits — point at safe scratch locations so settings_default's
# path-derived defaults resolve without needing a real gamedir.
GAME_DIR = tempfile.gettempdir()
LOG_DIR = os.path.join(tempfile.gettempdir(), "fcm_components_test_logs")
os.makedirs(LOG_DIR, exist_ok=True)

# The library is not added to INSTALLED_APPS: it registers no Django app, owns
# no models and runs no ``ready()``, so the entry would do nothing. The first
# component that needs an app registration adds it here and in installing.md.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "TEST": {"NAME": "file:fcm_components_test_default?mode=memory&cache=shared"},
    },
}

# Required Django bits
SECRET_KEY = "test-only-secret"
TEST_ENVIRONMENT = True
ROOT_URLCONF = "tests.urls"
