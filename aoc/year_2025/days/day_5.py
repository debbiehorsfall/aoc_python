from ...  import utils

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def merge_ranges(self, ranges):
        ranges_new = []
        for r in ranges:
           overlapping = False
           for i, n in enumerate(ranges_new):
               if ((n[0] <= r[0] <= n[1])
                   or (n[0] <= r[1] <= n[1])
                   or (r[0] <= n[1] <= r[1])
                   or (r[0] <= n[1] <= r[1])):
                   overlapping = True
                   ranges_new[i] = (min(r[0], n[0]), max(r[1], n[1]))

           if not overlapping:
               ranges_new.append(r)

        return ranges_new

    def calculate(self):
        sections = self.parser.get_sections_list()

        ranges = []
        for r in sections[0]:
            range_v = (int(r.split("-")[0]), int(r.split("-")[1]))
            ranges.append(range_v)

        self.sum = 0
        for i in sections[1]:
            value = int(i)
            if any(value >= x and value <= y for x, y in ranges):
                self.sum += 1

        while True:
            ranges_new = self.merge_ranges(ranges)
            if len(ranges_new) == len(ranges):
                break
            ranges = ranges_new

        self.count = sum(n[1]-n[0]+1 for n in ranges)

    def part_1(self):
        return self.sum

    def part_2(self):
        return self.count
