#!/usr/bin/python3

import re
from math import cos, sin
from math import radians as rad

def cruise(instructions, origin):
    def forward(bear):
        if bear == 0:
            return 'N'
        if bear == 90:
            return 'E'
        if bear == 180:
            return 'S'
        if bear == 270:
            return 'W'
    ops = { 'N': lambda arg: (x, y+arg, bear),
            'E': lambda arg: (x+arg, y, bear),
            'S': lambda arg: (x, y-arg, bear),
            'W': lambda arg: (x-arg, y, bear),
            'R': lambda arg: (x, y, (bear+arg)%360),
            'L': lambda arg: (x, y, (bear-arg)%360),
            'F': lambda arg: (ops[forward(bear)](arg)),
           }

    (x, y, bear) = origin
    for inst in instructions:
        x, y, bear = ops[inst[0]](int(inst[1]))
    return x, y, bear

def wp(instructions, origin):
    ops = { 'N': lambda arg: (x, y+arg, sx, sy),
            'E': lambda arg: (x+arg, y, sx, sy),
            'S': lambda arg: (x, y-arg, sx, sy),
            'W': lambda arg: (x-arg, y, sx, sy),
            'R': lambda arg: (round(x*cos(rad(-arg)) - y*sin(rad(-arg))),
                              round(x*sin(rad(-arg)) + y*cos(rad(-arg))),
                              sx, sy),
            'L': lambda arg: (round(x*cos(rad(arg)) - y*sin(rad(arg))),
                              round(x*sin(rad(arg)) + y*cos(rad(arg))),
                              sx, sy),
            'F': lambda arg: (x, y, sx+x*arg, sy+y*arg),
           }

    (x, y, sx, sy) = origin
    for inst in instructions:
        x, y, sx, sy = ops[inst[0]](int(inst[1]))
    return sx, sy

def manhattan_dist(x, y):
    return abs(x) + abs(y)

def run_pt1(data):
    p = re.compile(r'^([nsewlrf])(\d+)$', re.I)
    instructions = [ p.findall(line)[0] for line in data]
    orig = (0, 0, 90) # looking east
    x, y, bear = cruise(instructions, orig)
    return manhattan_dist(x, y)

def run_pt2(data):
    p = re.compile(r'^([nsewlrf])(\d+)$', re.I)
    instructions = [ p.findall(line)[0] for line in data]
    orig = (10, 1, 0, 0) # 10 east, 1 north
    x, y = wp(instructions, orig)
    return manhattan_dist(x, y)

if __name__ == '__main__':
    print(' BEGIN TEST '.center(80,'-'))
    test = ["F10", "N3", "F7", "R90", "F11"]
    print('Part one', run_pt1(test))
    print('Part two', run_pt2(test))
    print(' END TEST '.center(80,'-'))

    print(' BEGIN REAL '.center(80,'-'))
    with open('day12_input', 'r') as f:
        data = list(f)
        print('Part one', run_pt1(data))
        print('Part two', run_pt2(data))
    print(' END REAL '.center(80,'-'))
