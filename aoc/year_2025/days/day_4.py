from ...  import utils

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def remove_rolls(self, paper):
        remove = []
        for p in paper:
            count = sum(1 for n in utils.get_8_neighbours(p) if n in paper)
            if count < 4:
                remove.append(p)

        for r in remove:
            paper.remove(r)

        return len(remove)

    def calculate(self):
        lines = self.parser.get_lines()
        paper = utils.get_coords(lines, "@")

        removed = self.remove_rolls(paper)
        self.sum_1 = removed
        self.sum_2 = removed

        while removed != 0:
            removed = self.remove_rolls(paper)
            self.sum_2 += removed

    def part_1(self):
        return self.sum_1

    def part_2(self):
        return self.sum_2
