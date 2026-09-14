# Test plan — size

How big a thing is, and how two of them compare. Every creature and every physical object in the game
declares a size, and several systems read it — combat, spell targeting, item restriction, concealment,
and whether something fits through an exit.

The component owns **what sizes exist and how they order**. It owns none of the rules about what a
size *means*: fitting, bashing, holding and concealing each belong to the system that asks.

Code: `src/fcm_components/size.py`.
Tests: `src/fcm_components/tests/test_size.py`, runnable on their own with
`python runtests.py fcm_components.tests.test_size`.

An empty `Test function` cell is agreed behaviour not yet covered. Cases land here before the tests,
and the tests before the code.

## Fixtures

| Fixture | Purpose |
|---|---|

*(None. The component is pure functions over an enum.)*

## SZ — the sizes and their order

| ID | Case | Test function |
|---|---|---|
| SZ-01 | The set holds exactly six sizes — tiny, small, medium, large, huge, gargantuan | `SizesTest.test_the_set_holds_the_six_sizes` |
| SZ-02 | Every size has an ordering value, so none can be added without one | `SizesTest.test_every_size_has_an_ordering_value` |
| SZ-03 | Ordering values are distinct and ascend from tiny to gargantuan | `SizesTest.test_ordering_values_are_distinct_and_ascending` |

## SZ — reading a size's value

| ID | Case | Test function |
|---|---|---|
| SZ-04 | A size member returns its ordering value | `SizeValueTest.test_a_size_member_returns_its_ordering_value` |
| SZ-05 | The raw string a size is stored as returns the same value as the member | `SizeValueTest.test_the_raw_string_returns_the_same_value_as_the_member` |
| SZ-06 | Something that is not a size is refused rather than given a value | `SizeValueTest.test_something_that_is_not_a_size_is_refused` |

## SZ — comparing two sizes

| ID | Case | Test function |
|---|---|---|
| SZ-07 | A larger size is bigger than a smaller one, and the reverse is not | `SizeComparisonTest.test_a_larger_size_is_bigger_and_not_smaller` |
| SZ-08 | Two equal sizes are neither bigger nor smaller — both comparisons are strict | `SizeComparisonTest.test_equal_sizes_are_neither_bigger_nor_smaller` |
| SZ-09 | The comparisons take raw strings as well as members, on either side | `SizeComparisonTest.test_the_comparisons_take_raw_strings_on_either_side` |

## Open decisions

*(None.)*
