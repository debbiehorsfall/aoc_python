import pytest
from aoc.year_2025.days.day_5 import Day
from aoc.input_parser import ParserStub

LINES = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

def test_part_1():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_1() == 3)


def test_part_2():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_2() == 14)
