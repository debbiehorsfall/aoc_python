import pytest
from aoc.year_2025.days.day_6 import Day
from aoc.input_parser import ParserStub

LINES = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


def test_part_1():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_1() == 4277556)


def test_part_2():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_2() == 3263827)
