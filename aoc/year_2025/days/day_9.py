from ... import utils
from itertools import combinations
from collections import defaultdict

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        lines = self.parser.get_lines()
        coords = [(int(l.split(",")[0]), int(l.split(",")[1])) for l in lines]
        def area(a,b):
            return (abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1)


        def green(a,b):
            for c in coords:
                if min(a[1],b[1])<c[1]<max(a[1],b[1]):
                    for e in edges[c]:
                        if c[0] >= max(a[0], b[0]) and e[0] < max(a[0], b[0]):
                            return False
                        if c[0] <= min(a[0], b[0]) and e[0] > min(a[0], b[0]):
                            return False
                if min(a[0],b[0])<c[0]<max(a[0],b[0]):
                    for e in edges[c]:
                        if c[1] >= max(a[1], b[1]) and e[1] < max(a[1], b[1]):
                            return False
                        if c[1] <= min(a[1], b[1]) and e[1] > min(a[1], b[1]):
                            return False
            return True

        self.largest = max(area(a,b) for a,b in combinations(coords,2))

        edges = defaultdict(list)
        for i in range(len(coords)):
            edges[coords[i]].append(coords[(i+1)%len(coords)])
            edges[coords[(i+1)%len(coords)]].append(coords[i])
        self.largest_green = max(area(a,b) for a,b in combinations(coords,2) if green(a,b))

    def part_1(self):
        return self.largest

    def part_2(self):
        return self.largest_green
