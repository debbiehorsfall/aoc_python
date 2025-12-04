import pytest
from aoc.year_2025.days.day_3 import Day
from aoc.input_parser import ParserStub

LINES = """987654321111111
811111111111119
234234234234278
818181911112111"""

def test_part_1():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_1() == 357)


def test_part_2():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_2() == 3121910778619)
