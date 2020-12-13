#!/usr/bin/python3

import re
from itertools import count

def parse_schedule(data, pt2=False):
    p = re.compile(r'(\d+)')
    lines = p.findall(data[1])
    if pt2 == True:
        return { int(bus): idx for idx, bus in enumerate(data[1].split(',')) if bus != "x"}
    return int(data[0]), [ int(line) for line in lines ]

def run_pt1(data):
    arr, lines = parse_schedule(data)
    offsets = {line - (arr % line) : line for line in lines}
    wait = min(offsets.keys())
    return offsets[wait] * wait

def run_pt2(data):
    lines = parse_schedule(data, True)
    nums = sorted(lines.keys(), reverse=True)
    start_idx, st = 1, 1
    for current in nums[1:]:
        shift = (lines[nums[0]] - lines[current]) % current
        for idx in count(start_idx, st):
            if (nums[0] * idx) % current == shift:
                start_idx = idx
                st *= current
                break
    return nums[0] * start_idx - lines[nums[0]]


if __name__ == '__main__':
    print(' BEGIN TEST '.center(80,'-'))
    test = ["939", "7,13,x,x,59,x,31,19"]
    print('Part one', run_pt1(test))
    print('Part two', run_pt2(test))
    print(' END TEST '.center(80,'-'))

    print(' BEGIN REAL '.center(80,'-'))
    with open('day13_input', 'r') as f:
        data = list(f)
        print('Part one', run_pt1(data))
        print('Part two', run_pt2(data))
    print(' END REAL '.center(80,'-'))
