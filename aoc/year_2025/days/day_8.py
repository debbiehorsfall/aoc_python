from ... import utils
from collections import defaultdict, deque

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        lines = self.parser.get_lines()
        coords = [tuple(int(x) for x in l.split(",")) for l in lines]
        self.coords = coords
        self.distances = []
        for i in range(len(coords)-1):
            for j in range(i+1, len(coords)):
                distance = sum((coords[i][index]-coords[j][index])**2 for index in range(3))
                self.distances.append((coords[i], coords[j], distance))
        
        self.distances = sorted(self.distances, key=lambda item: item[2])
    
    def get_circuits(self, distances):
        circuits = []
        # Build adjacency list
        graph = defaultdict(set)
        for a, b, _ in distances:
            graph[a].add(b)
            graph[b].add(a)

        visited = set()
        circuits = []

        for node in graph:
            if node not in visited:
                queue = deque([node])
                group = set()

                while queue:
                    current = queue.popleft()
                    if current in visited:
                        continue
                    visited.add(current)
                    group.add(current)
                    queue.extend(graph[current])

                circuits.append(group)
        return circuits

    def shortest(self, num):
        circuits = self.get_circuits(self.distances[0:num])
        circuit_lens = sorted([len(s) for s in circuits])
        return circuit_lens[-1]*circuit_lens[-2]*circuit_lens[-3]
    
    def part_1(self):
        return self.shortest(1000)

    def first_span(self, num):
        for i in range(num,len(self.distances)):
            circuits = self.get_circuits(self.distances[0:i])
            if len(circuits) == 1 and len(circuits[0]) == len(self.coords):
                return self.distances[i-1][0][0]*self.distances[i-1][1][0]

    def part_2(self):
        return self.first_span(1000)
