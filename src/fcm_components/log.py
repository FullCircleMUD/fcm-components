# SPDX-License-Identifier: BSD-3-Clause
"""Logging shim for fcm-components.

Every line the library emits goes to its own ``components.log`` under
``settings.LOG_DIR``. The mechanism belongs to ``evennia-logging-extension``;
this file names the file and nothing else.

One file for the whole library rather than one per component: a component is
a module, not a deployable, and an operator tracing a call through two of them
should not have to open two logs.

Internal to the library, not part of the consumer-facing API.
"""

from evennia_logging_extension import make_logger

components_log = make_logger("components.log")
