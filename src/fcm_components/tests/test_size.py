# SPDX-License-Identifier: BSD-3-Clause
"""Unit tests for the size component.

Cases: docs/test-plans/size.md. A case lands there before the test here, and
the test before the code.

Runnable on its own:

    python runtests.py fcm_components.tests.test_size
"""

import unittest

from fcm_components.size import Size, bigger_than, size_value, smaller_than


class SizesTest(unittest.TestCase):
    """SZ — the sizes and their order."""

    def test_the_set_holds_the_six_sizes(self):
        """SZ-01 — tiny, small, medium, large, huge, gargantuan."""
        self.assertEqual(
            [size.value for size in Size],
            ["tiny", "small", "medium", "large", "huge", "gargantuan"],
        )

    def test_every_size_has_an_ordering_value(self):
        """SZ-02 — a size with no value raises at the first comparison."""
        self.assertTrue(list(Size), "no sizes to check — the loop below proves nothing")
        for size in Size:
            with self.subTest(size=size):
                self.assertIsInstance(size_value(size), int)

    def test_ordering_values_are_distinct_and_ascending(self):
        """SZ-03 — a duplicate would make two sizes compare as equal."""
        self.assertTrue(list(Size), "no sizes to check — the assertions below prove nothing")
        values = [size_value(size) for size in Size]
        self.assertEqual(len(values), len(set(values)))
        self.assertEqual(values, sorted(values))


class SizeValueTest(unittest.TestCase):
    """SZ — reading a size's value."""

    def test_a_size_member_returns_its_ordering_value(self):
        """SZ-04 — tiny is lowest, gargantuan is highest."""
        self.assertEqual(size_value(Size.TINY), 1)
        self.assertEqual(size_value(Size.GARGANTUAN), 6)

    def test_the_raw_string_returns_the_same_value_as_the_member(self):
        """SZ-05 — a size is stored on an object as its string."""
        self.assertTrue(list(Size), "no sizes to check — the loop below proves nothing")
        for size in Size:
            with self.subTest(size=size):
                self.assertEqual(size_value(size.value), size_value(size))

    def test_something_that_is_not_a_size_is_refused(self):
        """SZ-06 — no value is invented for it."""
        with self.assertRaises(ValueError):
            size_value("enormous")


class SizeComparisonTest(unittest.TestCase):
    """SZ — comparing two sizes."""

    def test_a_larger_size_is_bigger_and_not_smaller(self):
        """SZ-07 — and the reverse holds."""
        self.assertTrue(bigger_than(Size.HUGE, Size.SMALL))
        self.assertFalse(smaller_than(Size.HUGE, Size.SMALL))
        self.assertTrue(smaller_than(Size.SMALL, Size.HUGE))
        self.assertFalse(bigger_than(Size.SMALL, Size.HUGE))

    def test_equal_sizes_are_neither_bigger_nor_smaller(self):
        """SZ-08 — both comparisons are strict."""
        self.assertFalse(bigger_than(Size.MEDIUM, Size.MEDIUM))
        self.assertFalse(smaller_than(Size.MEDIUM, Size.MEDIUM))

    def test_the_comparisons_take_raw_strings_on_either_side(self):
        """SZ-09 — members and strings are interchangeable."""
        self.assertTrue(bigger_than("huge", Size.SMALL))
        self.assertTrue(bigger_than(Size.HUGE, "small"))
        self.assertTrue(bigger_than("huge", "small"))
        self.assertTrue(smaller_than("small", "huge"))
