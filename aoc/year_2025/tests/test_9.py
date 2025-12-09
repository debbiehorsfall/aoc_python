import pytest
from aoc.year_2025.days.day_9 import Day
from aoc.input_parser import ParserStub

LINES = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

def test_part_1():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_1() == 50)


def test_part_2():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_2() == 24)
