#!/usr/bin/python3

import string

def group_answers_any(group):
    seen = []
    for p in group:
        for a in p:
            if a not in seen:
                seen.append(a)
    return len(seen)

def group_answers_every(group):
    common = {}
    for p in group:
        for a in p:
            if a in common:
                common[a] += 1
            else:
                common[a] = 1
    al = 0
    for answ in common.values():
        if answ == len(group):
            al += 1
    return al

def run_pt2(data):
    count = 0
    for g in data:
        count += group_answers_every(g.split('\n'))
    return count

def run_pt1(data):
    count = 0
    for g in data:
        count += group_answers_any(g.split('\n'))
    return count

if __name__ == '__main__':
    print(' BEGIN TEST '.center(80,'-'))
    with open('day6_sample','r') as s:
        test = [grp for grp in s.read().split("\n\n") if grp]
        print('Part one', run_pt1(test))
        print('Part two', run_pt2(test))
    print(' END TEST '.center(80,'-'))

    print(' BEGIN REAL '.center(80,'-'))
    with open('day6_input', 'r') as f:
        data = [grp for grp in f.read().split("\n\n") if grp]
        print('Part one', run_pt1(data))
        print('Part two', run_pt2(data))
    print(' END REAL '.center(80,'-'))
