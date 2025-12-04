#!/usr/bin/python3

import os
from collections import namedtuple

def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func

def visited(func):
    visited = set()

    def visited_func(*args):
        if args in visited:
            return 0
        visited.add(args)
        result = func(*args)
        return result

    return visited_func

def add_coord(coord1, coord2):
    return tuple(x + y for x, y in zip(coord1, coord2))

def rotate(lines):
    return ["".join(line[i] for line in lines[::-1]) for i in range(len(lines))]

def flip(lines):
    return [line[::-1] for line in lines]

def get_coords(lines, char):
    coords = set()
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == char:
                coords.add((x,y))
    return coords

eight_incs = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
four_incs = [(0,1), (1,0), (0,-1), (-1,0)]

def get_4_neighbours(coord):
    return [add_coord(coord, i) for i in four_incs]

def get_8_neighbours(coord):
    return [add_coord(coord, i) for i in eight_incs]

