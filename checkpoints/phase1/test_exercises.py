"""Tests for the Phase 1 checkpoint. Don't edit this file; edit exercises.py.

Run from the repository root:  pytest checkpoints/phase1 -q
"""

import inspect
import itertools

import pytest

from exercises import (
    Rectangle,
    Square,
    Vector,
    column_totals,
    extract_emails,
    flatten,
    group_by,
    normalise_dates,
    parse_numbers,
    running_mean,
    top_n_words,
)


# Task 1 ---------------------------------------------------------------------
def test_top_n_words_example():
    assert top_n_words("the cat and The hat", 2) == [("the", 2), ("and", 1)]


def test_top_n_words_ties_and_punctuation():
    text = "Don't stop! Stop, don't... STOP."
    assert top_n_words(text, 3) == [("stop", 3), ("don", 2), ("t", 2)]


def test_top_n_words_n_larger_than_vocabulary():
    assert top_n_words("b a b", 10) == [("b", 2), ("a", 1)]


# Task 2 ---------------------------------------------------------------------
def test_flatten_deep():
    assert flatten([1, [2, [3, [4, [5]]]], [], 6]) == [1, 2, 3, 4, 5, 6]


def test_flatten_keeps_strings_whole():
    assert flatten(["ab", ["c", ["de"]]]) == ["ab", "c", "de"]


def test_flatten_empty():
    assert flatten([]) == []
    assert flatten([[], [[]]]) == []


# Task 3 ---------------------------------------------------------------------
def test_group_by_example_and_key_order():
    result = group_by(["apple", "bob", "avocado", "cherry", "blue"], key=lambda s: s[0])
    assert result == {"a": ["apple", "avocado"], "b": ["bob", "blue"], "c": ["cherry"]}
    assert list(result) == ["a", "b", "c"]


def test_group_by_numbers():
    assert group_by(range(7), key=lambda x: x % 3) == {0: [0, 3, 6], 1: [1, 4], 2: [2, 5]}


# Task 4 ---------------------------------------------------------------------
def test_running_mean_values():
    assert list(running_mean([2, 4, 9])) == [2.0, 3.0, 5.0]


def test_running_mean_is_generator():
    assert inspect.isgeneratorfunction(running_mean)


def test_running_mean_endless_stream():
    first_four = list(itertools.islice(running_mean(itertools.count(1)), 4))
    assert first_four == [1.0, 1.5, 2.0, 2.5]


# Task 5 ---------------------------------------------------------------------
def test_parse_numbers_example():
    assert parse_numbers(["1", " 2.5 ", "abc", "", "-3"]) == ([1.0, 2.5, -3.0], ["abc", ""])


def test_parse_numbers_all_good_and_all_bad():
    assert parse_numbers(["1e3", "0"]) == ([1000.0, 0.0], [])
    assert parse_numbers(["x", "1,000"]) == ([], ["x", "1,000"])


# Task 6 ---------------------------------------------------------------------
def test_vector_repr_len_abs():
    v = Vector(3, 4)
    assert repr(v) == "Vector(3, 4)"
    assert len(v) == 2
    assert abs(v) == 5.0
    assert isinstance(abs(v), float)
    assert repr(Vector(1.5, -2, 0)) == "Vector(1.5, -2, 0)"


def test_vector_arithmetic():
    assert Vector(3, 4) + Vector(1, 1) == Vector(4, 5)
    assert Vector(3, 4) * 2 == Vector(6, 8)
    assert Vector(1, 2, 3).dot(Vector(4, 5, 6)) == 32


def test_vector_equality():
    assert Vector(1, 2) == Vector(1, 2)
    assert Vector(1, 2) != Vector(2, 1)
    assert Vector(1, 2) != Vector(1, 2, 0)


def test_vector_add_does_not_mutate():
    a, b = Vector(1, 1), Vector(2, 2)
    a + b
    assert a == Vector(1, 1) and b == Vector(2, 2)


def test_vector_dimension_mismatch():
    with pytest.raises(ValueError):
        Vector(1, 2) + Vector(1, 2, 3)
    with pytest.raises(ValueError):
        Vector(1, 2).dot(Vector(1))


# Task 7 ---------------------------------------------------------------------
def test_rectangle_basics():
    r = Rectangle(3, 4)
    assert r.area() == 12
    assert r.perimeter == 14
    assert repr(r) == "Rectangle(width=3, height=4)"


def test_rectangle_perimeter_is_read_only():
    r = Rectangle(3, 4)
    with pytest.raises(AttributeError):
        r.perimeter = 100


def test_rectangle_from_string():
    r = Rectangle.from_string("3x4")
    assert isinstance(r, Rectangle)
    assert r.area() == 12.0
    for bad in ["3by4", "x4", "abc"]:
        with pytest.raises(ValueError):
            Rectangle.from_string(bad)


def test_square_inherits():
    s = Square(5)
    assert isinstance(s, Rectangle)
    assert s.area() == 25
    assert s.perimeter == 20
    assert repr(s) == "Square(side=5)"
    assert "area" not in Square.__dict__, "reuse Rectangle.area instead of redefining it"
    assert "perimeter" not in Square.__dict__, "reuse Rectangle.perimeter instead of redefining it"


def test_shapes_sort_by_area():
    shapes = [Rectangle(3, 4), Square(2), Rectangle(1, 1)]
    assert [s.area() for s in sorted(shapes)] == [1, 4, 12]


# Task 8 ---------------------------------------------------------------------
def test_extract_emails_example():
    text = ("Mail Ann.Lee@SMU.edu.sg or bob+news@example.com, "
            "not bob@localhost. Ann.lee@smu.edu.sg again")
    assert extract_emails(text) == ["ann.lee@smu.edu.sg", "bob+news@example.com"]


def test_extract_emails_trailing_punctuation_and_none():
    assert extract_emails("Write to x_y-z@mail-server.co.uk.") == ["x_y-z@mail-server.co.uk"]
    assert extract_emails("no addresses here @ all") == []


# Task 9 ---------------------------------------------------------------------
def test_normalise_dates_example():
    assert normalise_dates("Due 5/3/2026, paid 15/03/2026.") == "Due 2026-03-05, paid 2026-03-15."


def test_normalise_dates_leaves_other_text_alone():
    text = "Version 1/2 shipped on 12/11/2025; ratio 3/4."
    assert normalise_dates(text) == "Version 1/2 shipped on 2025-11-12; ratio 3/4."
    assert normalise_dates("nothing to do") == "nothing to do"


# Task 10 --------------------------------------------------------------------
def test_column_totals_example(tmp_path):
    path = tmp_path / "shop.csv"
    path.write_text("name,qty,price\na,2,1.5\nb,3,2.0\n")
    assert column_totals(path) == pytest.approx({"qty": 5.0, "price": 3.5})


def test_column_totals_skips_columns_with_gaps_or_text(tmp_path):
    path = tmp_path / "mixed.csv"
    path.write_text("id,score,note,bonus\n1,10.5,ok,\n2,-0.5,7,1\n3,5,8,2\n")
    assert column_totals(path) == pytest.approx({"id": 6.0, "score": 15.0})
