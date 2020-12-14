#!/usr/bin/python3

from collections import defaultdict
import re

def spread(x, i):
    a1 = 0
    a0 = 0
    for f in range(len(x)):
        if i & (1<<f) != 0:
            a1 |= 1<<x[f]
        else:
            a0 |= 1<<x[f]
    return a0,a1

def run_pt1(data):
    mem = defaultdict(int)
    for l in data:
        m = re.match(r'mask = ([X01]*)', l)
        if m:
            mask = m[1]
            ones = int(mask.translate(mask.maketrans("X", "0")), 2)
            zeros = int(mask.translate(mask.maketrans("X10", "001")), 2)
            x = [i for i,x in enumerate(reversed(mask))  if x == "X"]
        else:
            m = re.match(r'mem\[([0-9]+)\] = ([0-9]*)', l)
            addr = int(m[1])
            val = int(m[2])
            mem[addr] = val & ~zeros | ones

    return sum(mem.values())

def run_pt2(data):
    mem = defaultdict(int)
    for l in data:
        m = re.match(r'mask = ([X01]*)', l)
        if m:
            mask = m[1]
            ones = int(mask.translate(mask.maketrans("X", "0")), 2)
            zeros = int(mask.translate(mask.maketrans("X10", "001")), 2)
            x = [i for i,x in enumerate(reversed(mask))  if x == "X"]
        else:
            m = re.match(r'mem\[([0-9]+)\] = ([0-9]*)', l)
            addr = int(m[1])
            val = int(m[2])
            for i in range(1 << len(x)):
                a0, a1 = spread(x,i)
                mem[(addr | ones | a1) & ~a0] = val

    return sum(mem.values())


if __name__ == '__main__':
    print(' BEGIN TEST '.center(80,'-'))
    test = ["mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
            "mem[8] = 11", "mem[7] = 101", "mem[8] = 0"]
    test2 = ["mask = 000000000000000000000000000000X1001X",
             "mem[42] = 100",
             "mask = 00000000000000000000000000000000X0XX",
             "mem[26] = 1"]
    print('Part one', run_pt1(test))
    print('Part two', run_pt2(test2))
    print(' END TEST '.center(80,'-'))

    print(' BEGIN REAL '.center(80,'-'))
    with open('day14_input', 'r') as f:
        data = list(f)
        print('Part one', run_pt1(data))
        print('Part two', run_pt2(data))
    print(' END REAL '.center(80,'-'))
