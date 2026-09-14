# SPDX-License-Identifier: BSD-3-Clause
"""Size — how big a thing is, and how two of them compare.

Every creature and every physical object in the game declares a size, and
several systems read it: combat, spell targeting, item restriction,
concealment, and whether something fits through an exit.

This component owns **what sizes exist and how they order**, and nothing
about what a size means. Fitting, bashing, holding and concealing are each
the business of the system that asks — a ``fits_through()`` here would be
the exit's rule living in the wrong place.

Cases: docs/test-plans/size.md.
"""

from enum import Enum


class Size(str, Enum):
    """The sizes a thing can be, smallest to largest."""

    TINY = "tiny"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    HUGE = "huge"
    GARGANTUAN = "gargantuan"


#: Ordering, and the only reason a size can be compared to another. Distinct
#: values ascending with the declaration above: two sizes sharing one would
#: compare as equal in both directions.
_SIZE_VALUE = {
    Size.TINY: 1,
    Size.SMALL: 2,
    Size.MEDIUM: 3,
    Size.LARGE: 4,
    Size.HUGE: 5,
    Size.GARGANTUAN: 6,
}


def size_value(size):
    """Return numeric value for a size (1=tiny .. 6=gargantuan).

    Accepts ``Size`` members or the raw strings they are stored as, since an
    object holds its size as a string. Anything else raises ``ValueError``
    from ``Size()`` rather than being given a value it does not have.
    """
    return _SIZE_VALUE[Size(size)]


def bigger_than(check_size, reference_size):
    """True if check_size is strictly larger than reference_size."""
    return size_value(check_size) > size_value(reference_size)


def smaller_than(check_size, reference_size):
    """True if check_size is strictly smaller than reference_size."""
    return size_value(check_size) < size_value(reference_size)
