#!/usr/bin/python3

import re
"""
def get_col(line):
    colT = line[7:]
    col = range(8)
    for i in colT:
        if i == "R":
            col = col[len(col)//2:]
        if i == "L":
            col = col[:-(len(col)//2)]
    return col[0]

def get_row(line):
    rowT = line[:7]
    row = range(128)
    for i in rowT:
        if i == "B":
            row = row[len(row)//2:]
        if i == "F":
            row = row[:-len(row)//2]
    return row[0]

def gen_id(row, col):
    return row * 8 + col

def proc_line(line):
    row = get_row(line)
    col = get_col(line)
    seat_id = gen_id(row, col)
    return seat_id
"""
def bsp_to_id(bsp):
    hi = re.compile('B|R')
    lo = re.compile('F|L')
    binrep = hi.sub('1',bsp)
    binrep = lo.sub('0',binrep)
    return int(binrep, 2)

def run_pt2(data):
    ids = []
    for line in data:
        ids.append(bsp_to_id(line))
    for i in range(min(ids), max(ids)):
        if i not in ids:
            return i

def run_pt1(data):
    ids = []
    for line in data:
        ids.append(bsp_to_id(line))
    return max(ids)

if __name__ == '__main__':
    print(' BEGIN TEST '.center(80,'-'))
    test = [ 'BFFFBBFRRR',
             'FFFBBBFRRR',
             'BBFFBBFRLL'
            ]
    print('Part one', run_pt1(test))
    print('Part two', run_pt2(test))
    print(' END TEST '.center(80,'-'))

    print(' BEGIN REAL '.center(80,'-'))
    with open('day5_input', 'r') as f:
        grid = list(f)
        print('Part one', run_pt1(grid))
        print('Part two', run_pt2(grid))
    print(' END REAL '.center(80,'-'))
