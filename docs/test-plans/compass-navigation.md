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

## CN — parsing a direction out of player input

`parse_direction(text)` returns `(name, direction)`. It serves the commands that act on a thing in a
direction — `open`, `close`, `lock`, `unlock`, `picklock`, `disarm_trap` — so it is about doors as
much as exits. The direction comes back as its full name whichever form was typed; the name comes
back as whatever is left.

| ID | Case | Test function |
|---|---|---|
| CN-09 | A name followed by a direction splits into both — `door south` | `ParseDirectionTest.test_a_name_then_a_direction_splits_into_both` |
| CN-10 | A direction followed by a name splits into both — `south door` | `ParseDirectionTest.test_a_direction_then_a_name_splits_into_both` |
| CN-11 | An abbreviation returns the full direction name, in either position — `s door`, `door s` | `ParseDirectionTest.test_an_abbreviation_returns_the_full_direction_name` |
| CN-12 | A direction on its own returns an empty name and the direction | `ParseDirectionTest.test_a_direction_alone_returns_an_empty_name` |
| CN-13 | Input with no direction in it returns the whole input as the name and no direction | `ParseDirectionTest.test_input_with_no_direction_returns_the_whole_name` |
| CN-14 | A multi-word name with no direction stays whole — `iron gate` | `ParseDirectionTest.test_a_multi_word_name_with_no_direction_stays_whole` |
| CN-15 | A multi-word name with a direction keeps the name whole — `iron gate south` | `ParseDirectionTest.test_a_multi_word_name_with_a_direction_keeps_the_name_whole` |
| CN-16 | Input is matched case-insensitively — `Door South` | `ParseDirectionTest.test_input_is_matched_case_insensitively` |
| CN-17 | Empty or whitespace-only input returns an empty name and no direction | `ParseDirectionTest.test_empty_input_returns_an_empty_name_and_no_direction` |

## Open decisions

*(None.)*

Recorded so it is not re-raised: `parse_direction` is called **after** a literal search has failed,
never before. A name whose own words include a direction — `south gate` — splits if the parser sees
it first, and searching the input whole beforehand means it never does. The precondition is on the
docstring.
