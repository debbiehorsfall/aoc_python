class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        lines = self.parser.get_lines()
        pos = 50
        self.zero_count = 0
        self.count = 0
        for l in lines:
            factor = (1 if (l[0] == "R") else -1)
            inc = int(l[1:])
            if abs(inc) > 100:
                self.count += abs(inc) // 100
            new_pos = (pos + (factor * (inc % 100)))
            if new_pos % 100 == 0:
                self.zero_count += 1
                self.count += 1
            if new_pos > 100:
                self.count += 1
            if new_pos < 0 and pos != 0:
                self.count += 1
            pos = new_pos % 100

    def part_1(self):
        return self.zero_count

    def part_2(self):
        return self.count
