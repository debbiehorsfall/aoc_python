class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def repeat_two(self, string):
        return len(string) % 2 == 0 and string[:len(string)//2] == string[len(string)//2:]

    def repeat_n(self, string, n):
        if len(string) % n != 0:
            return False

        for i in range(1, len(string)//n):
            if string[0:n] != string[i*n:(i+1)*n]:
                return False
        return True

    def calculate(self):
        lines = self.parser.get_lines()

        self.two_sum = 0
        self.n_sum = 0

        for r in lines[0].split(","):
            start = int(r.split("-")[0])
            end = int(r.split("-")[1])
            for i in range(start, end+1):
                string = str(i)
                if self.repeat_two(string):
                    self.two_sum += i
                if any(self.repeat_n(string, n) for n in range(1, len(string)//2+1)):
                    self.n_sum += i

    def part_1(self):
        return self.two_sum

    def part_2(self):
        return self.n_sum
