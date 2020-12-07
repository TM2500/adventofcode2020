#!/usr/bin/python3

import collections
import re

def proc_input(lines):
    containedin = collections.defaultdict(set)
    contains = collections.defaultdict(list)
    for line in lines:
        color = re.match(r'(.+?) bags contain', line)[1]
        for ct, innercolor in re.findall(r'(\d+) (.+?) bags?[,.]', line):
            ct = int(ct)
            containedin[innercolor].add(color)
            contains[color].append((ct, innercolor))
    return containedin, contains

def cost(color, contains):
    total = 0
    for ct, inner in contains[color]:
        total += ct
        total += ct* cost(inner, contains)
    return total

def run_pt2(data):
    (containedin, contains) = proc_input(data)
    return cost('shiny gold', contains)

def run_pt1(data):
    (containedin, contains) = proc_input(data)
    hasgold = set()

    def check(color):
        for c in containedin[color]:
            hasgold.add(c)
            check(c)

    check('shiny gold')
    return len(hasgold)

if __name__ == '__main__':
    print(' BEGIN TEST '.center(80,'-'))
    with open('day7_sample','r') as s:
        test = list(s)
        print('Part one', run_pt1(test))
        print('Part two', run_pt2(test))
    print(' END TEST '.center(80,'-'))

    print(' BEGIN REAL '.center(80,'-'))
    with open('day7_input', 'r') as f:
        data = list(f)
        print('Part one', run_pt1(data))
        print('Part two', run_pt2(data))
    print(' END REAL '.center(80,'-'))
