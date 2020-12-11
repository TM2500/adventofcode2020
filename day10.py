#!/usr/bin/python3

from functools import reduce
from operator import mul

def run_pt1(data):
    nums = sorted(map(int, [l.strip() for l in data]))
    diff = list()
    for idx in range(1, len(nums)):
        diff.append(nums[idx] - nums[idx-1])
    return diff.count(3)+1, diff.count(1)+1, (diff.count(3)+1) * (diff.count(1)+1)

def run_pt2(data):
    nums = sorted(map(int, [l.strip() for l in data]))
    counts = ''.join(
        [str(max(1, c-nums[i-1])) for i, c in enumerate(nums)]).split('3')
    print(counts)
    per = [max(1, 2**(len(c)-1)) if len(c)<4 else 2**(len(c)-1)-1 for c in counts]
    return reduce(mul, per)

if __name__ == '__main__':
    print(' BEGIN TEST '.center(80,'-'))
    test = ["28", "33", "18", "42", "31",
            "14", "46", "20", "48", "47",
            "24", "23", "49", "45", "19",
            "38", "39", "11", "1", "32",
            "25", "35", "8", "17", "7",
            "9", "4", "2", "34", "10", "3"]
    print('Part one', run_pt1(test))
    print('Part two', run_pt2(test))
    print(' END TEST '.center(80,'-'))

    print(' BEGIN REAL '.center(80,'-'))
    with open('day10_input', 'r') as f:
        data = list(f)
        print('Part one', run_pt1(data))
        print('Part two', run_pt2(data))
    print(' END REAL '.center(80,'-'))
