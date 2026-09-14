# Installing

Everything a consuming game does to get `fcm-components` running, in the order it is done.

The list is short because the library ships no components yet. Each one that lands adds its own step —
a mixin to add to a typeclass, a setting to declare, a hook to answer — and the step goes here.

## 1. Install the package

Not published to PyPI. Clone and editable-install it into the same environment the game runs in:

```
git clone https://github.com/FullCircleMUD/fcm-components.git
cd fcm-components
pip install -e .
```

`evennia-logging-extension` is a hard dependency and is not on PyPI either. Editable-install it from
its own checkout first, and pip will treat it as satisfied.

## 2. Import it below the Evennia import in your settings module

Only relevant if something in your settings module reaches this library. `LOG_DIR` is set by
`from evennia.settings_default import *`, so an import above that line lands the log somewhere you did
not choose. Where the game overrides `LOG_DIR`, the override goes directly under that import — the
directory is resolved once, at the first library import.

## Required settings

None. The library reads no settings.

## Optional settings

None. The log filename is hardcoded to `components.log`.

## What is not checked for you

**Everything.** The library ships no `AppConfig` and no `check_settings()`, because it has nothing to
validate. Nothing about this install is verified at boot, and nothing will be until a component needs
a setting.

`INSTALLED_APPS` is the usual entry here and does not apply yet either: the library registers no
Django app, owns no models and runs no `ready()`. Adding it changes nothing. The first component that
needs an app registration brings the entry, the `AppConfig` and this section's real contents with it.
