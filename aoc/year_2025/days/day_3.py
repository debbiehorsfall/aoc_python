class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def max_str(self, string, n):
        if n == 1:
            return max(int(c) for c in string)

        max_char = str(max(int(c) for c in string[:len(string)-n+1]))
        return int(max_char + str(self.max_str(string[string.index(max_char)+1:], n-1)))

    def calculate(self):
        lines = self.parser.get_lines()
        self.sum = 0
        self.sum_p2 = 0
        for l in lines:
            l = l.strip("\n")
            self.sum += self.max_str(l, 2)
            self.sum_p2 += self.max_str(l, 12)

    def part_1(self):
        return self.sum

    def part_2(self):
        return self.sum_p2
