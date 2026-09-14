# Interoperability

This library against every sibling library in `libraries/`.

What this library does that can constrain a sibling: **nothing yet**. It ships no models, no migrations,
no database alias, no typeclass mixins, no commands, no scripts and no settings of its own. Its only
runtime behaviour is binding a log file through `evennia-logging-extension`.

That is why almost every section below is a clearance on the same grounds. **Each is revisited as its
own component lands** — a component that writes to the ORM, extends a typeclass or reads a setting
brings a real relationship with it, and the section it affects is rewritten then rather than left
standing on a clearance that has stopped being true.

## evennia-ai-memory

**No coupling.** Neither library imports the other. This library ships no code, so there is nothing to
embed, search or store.

## evennia-archive

**No coupling.** Neither library imports the other. This library ships no models and no object state,
so nothing it holds is in scope for archiving.

## evennia-calendar

**No coupling.** Neither library imports the other. This library reads no time, in-game or real.

## evennia-database-cascade

**No coupling.** This library owns no tables and declares no alias, so it has no spec and needs no
router. A component that later owns data takes the cascade on then, and this section is rewritten with
it.

## evennia-effects-conditions

**No coupling.** Neither library imports the other. This library applies nothing to a character.

## evennia-environment

**No coupling.** Neither library imports the other. This library holds no room or world state.

## evennia-equipment

**No coupling.** Neither library imports the other. This library ships no items and no wear or wield
state.

## evennia-llm-service

**No coupling.** Neither library imports the other. This library makes no model calls.

## evennia-logging-extension

**Hard dependency.** `log.py` binds `components_log` through `make_logger`, writing `components.log`
under `settings.LOG_DIR`. One log file for the library rather than one per component. The consumer's
side of this — where `LOG_DIR` is resolved and why a library import goes below the Evennia import in a
settings module — is in the extension's own
[docs/installing.md](../../evennia-logging-extension/docs/installing.md).

## evennia-message-bus

**No coupling.** Neither library imports the other. This library publishes and subscribes to nothing.

## evennia-mob-decision-engine

**No coupling.** Neither library imports the other. This library drives no mob behaviour.

## evennia-mob-spawner

**No coupling.** Neither library imports the other. This library spawns nothing and declares no spawn
rules.

## evennia-portal-multiplex

**No coupling.** Neither library imports the other. This library touches no Portal or Server class
setting, so there is nothing for it to layer over or be layered over by.

## evennia-procedural-dungeons

**No coupling.** Neither library imports the other. This library generates no world content.

## evennia-scaling

**No coupling.** Neither library imports the other. This library holds no per-instance state and
dispatches nothing between instances, so nothing it does is visible across a deployment.

## evennia-shards

**No coupling.** Neither library imports the other. `evennia-shards` is being deprecated in favour of
`evennia-scaling`, and this library targets neither.

## evennia-survival

**No coupling.** Neither library imports the other. This library ships no meters and no tick.

## evennia-targeting

**No coupling.** Neither library imports the other, so this library has no `targeting.py` and declares
no `p_`, `f_` or `op_` names. A component that later takes the dependency gets one, and every such
callable in this repository goes in it.

## evennia-world-builder

**No coupling.** Neither library imports the other. This library reads no world definitions and
contributes no typeclasses for one to instantiate.

## evennia-yaml-reader

**No coupling.** Neither library imports the other. This library reads no YAML.

## fcm-components

This library.

## fcm-subscriptions

**No coupling.** Neither library imports the other. This library answers no access question and holds
no account state.

## fcm-telemetry-spawn

**No coupling.** Neither library imports the other. This library emits no telemetry.

## fcm-xrpl

**No coupling.** Neither library imports the other. This library touches no wallet, no ledger and no
on-chain state.
