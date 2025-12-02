import pytest
from aoc.year_2025.days.day_2 import Day
from aoc.input_parser import ParserStub

LINES = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
"""

def test_part_1():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_1() == 1227775554)


def test_part_2():
    d = Day(ParserStub(LINES))
    d.calculate()
    assert (d.part_2() == 4174379265)
