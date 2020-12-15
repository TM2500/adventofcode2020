#!/usr/bin/python3

from collections import deque

def play(n, num, start_num_count, num_idx):
    for i in range(start_num_count, n):
        last = num[-1]

        if len(num_idx[last]) >= 2:
            last_spoken = num_idx[last][1]
            last_last_spoken = num_idx[last][0]
            new = last_spoken - last_last_spoken
        else:
            new = 0
        num.append(new)

        if new not in num_idx:
            num_idx[new] = deque(maxlen=2)

        num_idx[new].append(i)

    return new

def run_pt1(data):
    num = list(map(int, data[0].split(",")))
    num_idx = {number: deque([i], maxlen=2) for i, number in enumerate(num)}
    start_num_count = len(num_idx)
    return play(2020, num, start_num_count, num_idx)

def run_pt2(data):
    num = list(map(int, data[0].split(",")))
    num_idx = {number: deque([i], maxlen=2) for i, number in enumerate(num)}
    start_num_count = len(num_idx)
    return play(30000000, num, start_num_count, num_idx)

if __name__ == '__main__':
    print(' BEGIN TEST '.center(80,'-'))
    test = ["1,3,2"]
    test2 = ["2,1,3"]
    print('Part one', run_pt1(test), run_pt1(test2))
    print('Part two', run_pt2(test))
    print(' END TEST '.center(80,'-'))

    print(' BEGIN REAL '.center(80,'-'))
    with open('day15_input', 'r') as f:
        data = list(f)
        print('Part one', run_pt1(data))
        print('Part two', run_pt2(data))
    print(' END REAL '.center(80,'-'))
