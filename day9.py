#!/usr/bin/python3

import itertools as ite

def valid(idx, pre, nums):
    assert(pre-1 < idx < len(nums))
    preamble = nums[idx-pre:idx]
    vals = [sum(i) for i in ite.combinations(preamble,2) if sum(i) == nums[idx]]
    if len(vals) == 0:
        return idx
    return -1

def find_set(val, nums):
    for i in range(2, len(nums)):
        for j in range(i+1, len(nums)):
            sub = nums[i:j]
            if sum(sub) == val:
                sub = sorted(sub)
                return sub[0] + sub[-1]
    return -1

def run_pt1(data, pre):
    nums = [ n for n in map(int, [l.strip() for l in data])]
    return [ nums[i] for i in range(pre, len(nums)) if valid(i, pre, nums) > 0][0]

def run_pt2(data, pre):
    nums = [ n for n in map(int, [l.strip() for l in data])]
    return find_set(run_pt1(data, pre), nums)

if __name__ == '__main__':
    print(' BEGIN TEST '.center(80,'-'))
    test = ["35", "20", "15", "25",
            "47", "40", "62", "55",
            "65", "95", "102", "117",
            "150", "182", "127", "219",
            "299", "277", "309", "576" ]
    print('Part one', run_pt1(test, 5))
    print('Part two', run_pt2(test, 5))
    print(' END TEST '.center(80,'-'))

    print(' BEGIN REAL '.center(80,'-'))
    with open('day9_input', 'r') as f:
        data = list(f)
        print('Part one', run_pt1(data, 25))
        print('Part two', run_pt2(data, 25))
    print(' END REAL '.center(80,'-'))
