#!/usr/bin/python3

from itertools import product
from collections import defaultdict

def parse_initial(data):
    return set((r, c) for r, line in enumerate(data)
               for c, n in enumerate(line) if n == '#')

def cnt_active(active, dimension=3, cycles=6):
    active = set((0,) * (dimension-2) + cube for cube in active)
    for _ in range(cycles):
        new_active = set()
        neighbours = defaultdict(int)
        for cube in active:
            for offset in product((-1, 0, 1), repeat=dimension):
                if offset != (0,) * dimension:
                    neighbour = tuple(x + dx for x, dx in zip(cube, offset))
                    neighbours[neighbour] += 1

        for cube, n in neighbours.items():
            if cube in active and n in [2,3]:
                new_active.add(cube)

            elif cube not in active and n == 3:
                new_active.add(cube)

        active = new_active
    return len(active)

def run_pt1(data):
    active = parse_initial(data)
    return cnt_active(active)

def run_pt2(data):
    active = parse_initial(data)
    return cnt_active(active, 4)

if __name__ == '__main__':
    print(' BEGIN TEST '.center(80,'-'))
    test = [".#.", "..#", "###"]
    print('Part one', run_pt1(test))
    print('Part two', run_pt2(test))
    print(' END TEST '.center(80,'-'))

    print(' BEGIN REAL '.center(80,'-'))
    with open('day17_input', 'r') as f:
        data = [ line.strip() for line in f.readlines()]
        print('Part one', run_pt1(data))
        print('Part two', run_pt2(data))
    print(' END REAL '.center(80,'-'))
