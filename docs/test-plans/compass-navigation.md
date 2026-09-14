# Test plan — compass navigation

The game navigates by compass. This component provides the mechanism.

Code: `src/fcm_components/compass_navigation.py`.
Tests: `src/fcm_components/tests/test_compass_navigation.py`, runnable on their own with
`python runtests.py fcm_components.tests.test_compass_navigation`.

An empty `Test function` cell is agreed behaviour not yet covered. Cases land here before the tests,
and the tests before the code.

## Fixtures

| Fixture | Purpose |
|---|---|
| `_Caller` | A stand-in for a builder, carrying only `msg()` and a record of what it was told. The locked commands need nothing else of their caller |

## CN — the directions

The set of directions the game navigates by, and what each one carries.

| ID | Case | Test function |
|---|---|---|
| CN-01 | The set holds exactly twelve directions — the eight compass points, up, down, in and out | `DirectionsTest.test_the_set_holds_the_twelve_directions` |
| CN-02 | Each direction carries its full name, its abbreviation, its opposite and its display order, all four present | `DirectionsTest.test_every_direction_carries_all_four_fields` |
| CN-03 | Opposites are reciprocal — the opposite of each direction's opposite is itself | `DirectionsTest.test_opposites_are_reciprocal` |
| CN-04 | No two directions share a display order value, so the sort is deterministic | `DirectionsTest.test_no_two_directions_share_a_display_order` |

## CN — the building commands are locked

FCM does not build rooms or exits in game. The component replaces `@dig`, `@tunnel` and `@open` with
commands that refuse, so none of them can create a room, an exit or an alias.

| ID | Case | Test function |
|---|---|---|
| CN-05 | `@dig` refuses, and nothing is created | `LockedBuildingCommandsTest.test_dig_refuses_and_creates_nothing` |
| CN-06 | `@tunnel` refuses, and nothing is created | `LockedBuildingCommandsTest.test_tunnel_refuses_and_creates_nothing` |
| CN-07 | Each refusal says how FCM rooms are actually built, so a builder is not left guessing | `LockedBuildingCommandsTest.test_the_refusal_says_how_rooms_are_built` |
| CN-08 | `@open` refuses, and nothing is created | `LockedBuildingCommandsTest.test_open_refuses_and_creates_nothing` |

## Open decisions

*(None.)*
