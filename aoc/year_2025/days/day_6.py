from functools import reduce

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        self.lines = self.parser.get_lines()

    def part_1(self):
        x = 0
        for i in range(len(self.lines[0].split())):
            operator = self.lines[-1].split()[i]
            if operator == "*":
                x += reduce(lambda x, y: x * y, (int(l.split()[i]) for l in self.lines[:-1]))
            elif operator == "+":
                x += sum(int(l.split()[i]) for l in self.lines[:-1])
            else:
                assert(False)
        return x

    def part_2(self):
        x = 0
        operators = []
        for i, char in enumerate(self.lines[-1]):
            if char == "*" or char == "+":
                operators.append((char, i))

        for i, (operator, start) in enumerate(operators):
            if i == len(operators)-1:
                end = len(self.lines[0])
            else:
                end = operators[i+1][1]-1

            nums = []
            for pos in range(start, end):
                num_str = "".join(l[pos] for l in self.lines[:-1]).strip()
                if num_str:
                    nums.append(int(num_str))

            print(operator)
            print(nums)

            if operator == "*":
                x += reduce(lambda x, y: x * y, nums)
            elif operator == "+":
                x += sum(nums)
            else:
                assert(False)

        return x
