# SPDX-License-Identifier: BSD-3-Clause
"""Compass navigation — the directions FCM moves by, and the lock that holds it there.

The game navigates by compass. This module owns the closed set of directions
that means, what each one carries, and the replacement building commands that
stop a room or an exit being created outside the world source.

Cases: docs/test-plans/compass-navigation.md.
"""

from dataclasses import dataclass

# The building commands are subclassed rather than reimplemented so the
# replacements inherit Evennia's keys, aliases, locks and help entries — a
# builder typing the command reaches ours, not the one that builds.
from evennia.commands.default.building import (
    CmdDig as _EvenniaCmdDig,
    CmdOpen as _EvenniaCmdOpen,
    CmdTunnel as _EvenniaCmdTunnel,
)


@dataclass(frozen=True)
class Direction:
    """One direction the game navigates by.

    ``order`` is the position in a rendered exit line, not a compass bearing.
    Every direction's value is distinct, so sorting on it is deterministic.
    """

    name: str
    abbreviation: str
    opposite: str
    order: int


def _build(rows):
    """Turn (name, abbreviation, opposite) rows into the keyed table.

    Order comes from the row's position, which is what makes the declaration
    below the single statement of display order — there is no second list to
    fall out of step with it.
    """
    return {
        name: Direction(name, abbreviation, opposite, order)
        for order, (name, abbreviation, opposite) in enumerate(rows)
    }


#: Every direction FCM navigates by, keyed by full name. Declaration order is
#: display order: the four compass points, then the diagonals, then vertical,
#: then in and out.
DIRECTIONS = _build(
    [
        ("north", "n", "south"),
        ("east", "e", "west"),
        ("south", "s", "north"),
        ("west", "w", "east"),
        ("northeast", "ne", "southwest"),
        ("northwest", "nw", "southeast"),
        ("southeast", "se", "northwest"),
        ("southwest", "sw", "northeast"),
        ("up", "u", "down"),
        ("down", "d", "up"),
        ("in", "i", "out"),
        ("out", "o", "in"),
    ]
)

#: What a builder is told when they try to build in game. It names where rooms
#: actually come from, because "you can't do that" without a destination is
#: what sends someone looking through help files.
BUILD_REFUSED = (
    "Rooms and exits are not built in game. They come from the world source — "
    "add them there and rebuild."
)


class _LockedBuildCommand:
    """Refuses, and says where to go instead.

    Mixed in ahead of Evennia's command so this ``func`` is the one that runs.
    It does not call ``super()``: blocking the chain is the whole job, and
    calling up would run the build this exists to prevent.
    """

    def func(self):
        from .log import components_log

        components_log(
            f"{type(self).__name__} refused for {self.caller}: building in game is locked."
        )
        self.caller.msg(BUILD_REFUSED)


class CmdDig(_LockedBuildCommand, _EvenniaCmdDig):
    """Locked. Rooms come from the world source."""


class CmdTunnel(_LockedBuildCommand, _EvenniaCmdTunnel):
    """Locked. Rooms come from the world source."""


class CmdOpen(_LockedBuildCommand, _EvenniaCmdOpen):
    """Locked. Exits come from the world source."""
