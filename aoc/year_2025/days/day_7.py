from ... import utils

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        lines = self.parser.get_lines()
        coords = utils.get_coords(lines, "S")
        assert(len(coords) == 1)

        splitters = utils.get_coords(lines, "^")
        
        self.count = 0
        coords = list(utils.get_coords(lines, "S"))
        assert(len(coords) == 1)
        coords = {coords[0]: 1}

        splitters_hit = set()
        for _ in range(len(lines)):
            new_coords = {}
            for coord, count in coords.items():
                new_coord = utils.add_coord(coord, (0,1))
                if new_coord in splitters:
                    splitters_hit.add(new_coord)
                    next = [utils.add_coord(new_coord, (1,0)), utils.add_coord(new_coord, (-1,0))]
                else:
                    next = [new_coord]
                print(next)
                for n in next:
                    if n in new_coords:
                        new_coords[n] += count
                    else:
                        new_coords[n] = count
            coords = new_coords
        
        self.splitters_hit = len(splitters_hit)
        self.paths = sum(coords.values())

    def part_1(self):
        return self.splitters_hit

    def part_2(self):
        return self.paths
