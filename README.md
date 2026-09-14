# fcm-components

FCM's shared components, for [Evennia](https://www.evennia.com/) games — one module per component.

FullCircleMUD is being decomposed into libraries so that every system has a stated boundary, a stated
interface and findable consumers. Some of what that decomposition turns up is too small to be a library
of its own: a mixin, a helper, a piece with an important job and few moving parts. Those live here, one
module each.

A component in here is also a library that has not proved it needs to be one yet. Building it as a
module does the thinking work first; if it outgrows the slot, it moves out into its own repository.

## Status

**Scaffolded, no components yet.** The repository structure, the test runner and the documentation
surfaces are in place; nothing has been extracted into it. See [docs/progress.md](docs/progress.md).

## Is this for me?

Probably not, and that is deliberate.

FCM concepts are embedded in this library and are not abstracted out, which is what the `fcm-` prefix
is there to say. Unlike its `evennia-*` siblings it makes no claim to drop into an arbitrary Evennia
install. It is BSD-3-Clause and readable — it is just not aimed at you.

## Install

Not published to PyPI. From a checkout, into the same environment your game runs in:

```
git clone https://github.com/FullCircleMUD/fcm-components.git
cd fcm-components
pip install -e .
```

`evennia-logging-extension` is not on PyPI either — editable-install it from its own checkout first,
and pip will treat it as satisfied.

## Setup

**[docs/installing.md](docs/installing.md)** is the step list, along with the settings the library
reads and what is not checked for you.

## Learn more

- **[docs/INDEX.md](docs/INDEX.md)** — index of design documents.
- **[docs/test-plans/INDEX.md](docs/test-plans/INDEX.md)** — every behaviour the library commits to,
  one plan per component, and the test covering each case.
- **[docs/interoperability.md](docs/interoperability.md)** — how this library sits alongside its
  siblings.
- **[CLAUDE.md](CLAUDE.md)** — load-bearing principles, for working in the repository itself.

## License

BSD 3-Clause. See [LICENSE](LICENSE).
