# SPDX-License-Identifier: BSD-3-Clause
"""Unit tests for the compass_navigation component.

Cases: docs/test-plans/compass-navigation.md. A case lands there before the
test here, and the test before the code.

Runnable on its own:

    python runtests.py fcm_components.tests.test_compass_navigation
"""

import unittest

from fcm_components.compass_navigation import (
    DIRECTIONS,
    CmdDig,
    CmdOpen,
    CmdTunnel,
    parse_direction,
)


class _Caller:
    """A stand-in for a builder. The locked commands want nothing but msg()."""

    def __init__(self):
        self.messages = []

    def msg(self, text="", **kwargs):
        self.messages.append(str(text))


class DirectionsTest(unittest.TestCase):
    """CN — the directions."""

    def test_the_set_holds_the_twelve_directions(self):
        """CN-01 — eight compass points, up, down, in and out."""
        self.assertEqual(
            set(DIRECTIONS),
            {
                "north", "northeast", "east", "southeast",
                "south", "southwest", "west", "northwest",
                "up", "down", "in", "out",
            },
        )

    def test_every_direction_carries_all_four_fields(self):
        """CN-02 — name, abbreviation, opposite and display order."""
        for name, direction in DIRECTIONS.items():
            with self.subTest(direction=name):
                self.assertEqual(direction.name, name)
                self.assertTrue(direction.abbreviation)
                self.assertTrue(direction.opposite)
                self.assertIsInstance(direction.order, int)

    def test_opposites_are_reciprocal(self):
        """CN-03 — the opposite of a direction's opposite is itself."""
        for name, direction in DIRECTIONS.items():
            with self.subTest(direction=name):
                self.assertIn(direction.opposite, DIRECTIONS)
                self.assertEqual(DIRECTIONS[direction.opposite].opposite, name)

    def test_no_two_directions_share_a_display_order(self):
        """CN-04 — a duplicate order makes the sort non-deterministic."""
        orders = [direction.order for direction in DIRECTIONS.values()]
        self.assertEqual(len(orders), len(set(orders)))


class LockedBuildingCommandsTest(unittest.TestCase):
    """CN — the building commands are locked."""

    def _run(self, command_class):
        """Run a locked command and return (caller, whether it called through)."""
        caller = _Caller()
        command = command_class()
        command.caller = caller
        command.args = " Kitchen = north;n"
        command.switches = []
        called_through = []
        command.execute_cmd = lambda *a, **kw: called_through.append(a)
        command.func()
        return caller, called_through

    def test_dig_refuses_and_creates_nothing(self):
        """CN-05 — @dig builds nothing."""
        caller, called_through = self._run(CmdDig)
        self.assertTrue(caller.messages)
        self.assertEqual(called_through, [])

    def test_tunnel_refuses_and_creates_nothing(self):
        """CN-06 — @tunnel builds nothing, and never reaches @dig."""
        caller, called_through = self._run(CmdTunnel)
        self.assertTrue(caller.messages)
        self.assertEqual(called_through, [])

    def test_the_refusal_says_how_rooms_are_built(self):
        """CN-07 — a builder is told where to go instead."""
        for command_class in (CmdDig, CmdTunnel, CmdOpen):
            with self.subTest(command=command_class.__name__):
                caller, _ = self._run(command_class)
                self.assertIn("world source", " ".join(caller.messages).lower())

    def test_open_refuses_and_creates_nothing(self):
        """CN-08 — @open builds no exit between existing rooms."""
        caller, called_through = self._run(CmdOpen)
        self.assertTrue(caller.messages)
        self.assertEqual(called_through, [])


class ParseDirectionTest(unittest.TestCase):
    """CN — parsing a direction out of player input."""

    def test_a_name_then_a_direction_splits_into_both(self):
        """CN-09 — `door south`."""
        self.assertEqual(parse_direction("door south"), ("door", "south"))

    def test_a_direction_then_a_name_splits_into_both(self):
        """CN-10 — `south door`."""
        self.assertEqual(parse_direction("south door"), ("door", "south"))

    def test_an_abbreviation_returns_the_full_direction_name(self):
        """CN-11 — in either position."""
        self.assertEqual(parse_direction("s door"), ("door", "south"))
        self.assertEqual(parse_direction("door s"), ("door", "south"))

    def test_a_direction_alone_returns_an_empty_name(self):
        """CN-12 — the whole input was the direction."""
        self.assertEqual(parse_direction("south"), ("", "south"))
        self.assertEqual(parse_direction("s"), ("", "south"))

    def test_input_with_no_direction_returns_the_whole_name(self):
        """CN-13 — nothing to split."""
        self.assertEqual(parse_direction("chest"), ("chest", None))

    def test_a_multi_word_name_with_no_direction_stays_whole(self):
        """CN-14 — `iron gate`."""
        self.assertEqual(parse_direction("iron gate"), ("iron gate", None))

    def test_a_multi_word_name_with_a_direction_keeps_the_name_whole(self):
        """CN-15 — `iron gate south`."""
        self.assertEqual(parse_direction("iron gate south"), ("iron gate", "south"))

    def test_input_is_matched_case_insensitively(self):
        """CN-16 — `Door South`."""
        self.assertEqual(parse_direction("Door South"), ("door", "south"))

    def test_empty_input_returns_an_empty_name_and_no_direction(self):
        """CN-17 — nothing typed, nothing found."""
        self.assertEqual(parse_direction(""), ("", None))
        self.assertEqual(parse_direction("   "), ("", None))
