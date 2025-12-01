import pytest
from aoc.year_2025.days.day_1 import Day
from aoc.input_parser import ParserStub

LINES = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def test_part_1():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_1() == 3)


def test_part_2():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_2() == 6)
