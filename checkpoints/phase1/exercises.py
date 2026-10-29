"""Phase 1 checkpoint: Python fundamentals.

Replace every `raise NotImplementedError` below with your own code, then run
this from the repository root:

    pytest checkpoints/phase1 -q

Rules
- Set a 2-hour timer.
- You may use the official Python docs (https://docs.python.org/3/).
- Don't search for solutions, don't use an AI assistant, and don't copy from
  your earlier work.
- Each task names the course unit that teaches it. If a test fails, go back
  to that unit and then try again.

You pass when all the tests pass inside the timebox.
"""

import csv
import re


# ---------------------------------------------------------------------------
# Task 1 - strings, dicts, sorting with a key (Units 1.2-1.4)
# ---------------------------------------------------------------------------
def top_n_words(text, n):
    """Return the n most common words in `text` as a list of (word, count) tuples.

    A word is a run of the letters a-z, matched case-insensitively and
    returned in lower case, so "Don't" counts as "don" and "t". Sort by count,
    highest first, and break ties alphabetically.

    >>> top_n_words("the cat and The hat", 2)
    [('the', 2), ('and', 1)]
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Task 2 - recursion and lists (Units 1.3, 1.5)
# ---------------------------------------------------------------------------
def flatten(nested):
    """Flatten lists nested to any depth into a single list, keeping the order.

    Only lists are unpacked. Other values, strings included, are kept as they are.

    >>> flatten([1, [2, [3, 4]], [], 5])
    [1, 2, 3, 4, 5]
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Task 3 - functions as arguments, dicts (Units 1.4-1.5)
# ---------------------------------------------------------------------------
def group_by(items, key):
    """Group `items` into a dict that maps key(item) to a list of items.

    Keys appear in the order they are first seen, and the items in each list
    keep their original order.

    >>> group_by(["apple", "bob", "avocado"], key=lambda s: s[0])
    {'a': ['apple', 'avocado'], 'b': ['bob']}
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Task 4 - generators (Unit 1.5)
# ---------------------------------------------------------------------------
def running_mean(numbers):
    """Yield the mean of all the numbers seen so far, once per input number.

    This must be a generator (use `yield`) so that it also works on an
    endless stream such as itertools.count().

    >>> list(running_mean([2, 4, 9]))
    [2.0, 3.0, 5.0]
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Task 5 - exceptions (Units 1.5, 2.1)
# ---------------------------------------------------------------------------
def parse_numbers(values):
    """Convert strings to floats and skip the ones that can't be converted.

    Return a tuple (numbers, bad). `numbers` is the list of floats and `bad`
    is the list of strings that failed, both in input order. Surrounding
    whitespace is ignored. Use try/except rather than checking the strings
    yourself.

    >>> parse_numbers(["1", " 2.5 ", "abc", "", "-3"])
    ([1.0, 2.5, -3.0], ['abc', ''])
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Task 6 - classes and dunder methods (Units 2.2-2.4)
# ---------------------------------------------------------------------------
class Vector:
    """A vector with any number of components.

    >>> v = Vector(3, 4)
    >>> v
    Vector(3, 4)
    >>> len(v)
    2
    >>> abs(v)              # Euclidean length, always a float
    5.0
    >>> v + Vector(1, 1)
    Vector(4, 5)
    >>> v * 2               # multiply by a number
    Vector(6, 8)
    >>> v.dot(Vector(1, 0))
    3
    >>> Vector(1, 2) == Vector(1, 2)
    True

    Adding vectors of different lengths, or taking their dot product, raises
    ValueError.
    """

    def __init__(self, *components):
        raise NotImplementedError


# ---------------------------------------------------------------------------
# Task 7 - inheritance, properties, classmethods (Units 2.3-2.4)
# ---------------------------------------------------------------------------
class Rectangle:
    """A rectangle with a width and a height.

    - area() returns width * height.
    - perimeter is a read-only property (use @property), so assigning to it
      raises AttributeError.
    - Rectangle.from_string("3x4") is an alternative constructor (a
      classmethod) that returns Rectangle(3.0, 4.0). It raises ValueError for
      input it can't parse, such as "3by4" or "x4".
    - Rectangles compare by area with <, so sorted(list_of_rectangles) works.
    - repr(Rectangle(3, 4)) == "Rectangle(width=3, height=4)"
    """

    def __init__(self, width, height):
        raise NotImplementedError


class Square(Rectangle):
    """A rectangle whose sides are all equal, created with Square(side).

    Inherit from Rectangle and reuse its methods. Don't redefine area() or
    perimeter.
    repr(Square(5)) == "Square(side=5)"
    """

    def __init__(self, side):
        raise NotImplementedError


# ---------------------------------------------------------------------------
# Task 8 - regular expressions: findall (Units 2.5-2.6)
# ---------------------------------------------------------------------------
def extract_emails(text):
    """Return the unique email addresses in `text`, in lower case, in the order
    they first appear.

    An address is:
    - one or more letters, digits, or the characters . _ % + -
    - then "@"
    - then a domain made of letters, digits, hyphens and dots, which ends in
      a dot followed by at least two letters.

    >>> extract_emails("Mail Ann.Lee@SMU.edu.sg or bob+news@example.com, "
    ...                "not bob@localhost. Ann.lee@smu.edu.sg again")
    ['ann.lee@smu.edu.sg', 'bob+news@example.com']
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Task 9 - regular expressions: groups and sub (Units 2.5-2.6)
# ---------------------------------------------------------------------------
def normalise_dates(text):
    """Rewrite every DD/MM/YYYY date in `text` as YYYY-MM-DD and leave the rest
    of the text unchanged.

    The day and month may have one or two digits. Pad both to two digits.

    >>> normalise_dates("Due 5/3/2026, paid 15/03/2026.")
    'Due 2026-03-05, paid 2026-03-15.'
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Task 10 - files and the csv module (Unit 1.6)
# ---------------------------------------------------------------------------
def column_totals(path):
    """Read the CSV file at `path`, which has a header row, and return a dict
    that maps each column name to the float sum of that column.

    Include only the columns where every value is a number. Leave out any
    column with a non-numeric or empty value. Use the standard library's csv
    module, not pandas.

    For a file containing
        name,qty,price
        a,2,1.5
        b,3,2.0
    the result is {'qty': 5.0, 'price': 3.5}.
    """
    raise NotImplementedError
