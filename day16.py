#!/usr/bin/python3

import re

def get_def(data):
    stop_idx = data.index('')
    p = re.compile(r'^(.*): (\d+-\d+) or (\d+-\d+)', re.I)
    ticket_def = {}
    for line in data[:stop_idx]:
        m = p.fullmatch(line)
        g1 = [ int(el) for el in m.group(2).split('-')]
        g2 = [ int(el) for el in m.group(3).split('-')]
        ticket_def[m.group(1)] = ( range(g1[0], g1[1]+1), range(g2[0], g2[1]+1))
    return ticket_def, stop_idx

def get_my_ticket(data):
    return [int(el) for el in data[1].split(',')]

def get_others(data):
    stop_idx = data.index('nearby tickets:')
    tickets = [ [int(el) for el in line.split(',')] for line in data[stop_idx+1:] ]
    return tickets

def is_invalid(t, fields):
    for v in t:
        wrong = True
        for r1, r2 in fields.values():
            if v in r1 or v in r2:
                wrong = False
                break
            if wrong:
                continue
    return False

def run_pt1(data):
    t, ticket_idx = get_def(data)
    my_ticket = get_my_ticket(data[ticket_idx+1:])
    others = get_others(data)
    err = 0
    for ticket in others:
        for el in ticket:
            has_def = -1
            for r1, r2 in t.values():
                if el in r1 or el in r2:
                    has_def = 1
            if has_def < 0:
                err += el
    return err

def run_pt2(data):
    return "Run day16_2.go!"

if __name__ == '__main__':
    print(' BEGIN TEST '.center(80,'-'))
    test = ["class: 1-3 or 5-7", "row: 6-11 or 33-44", "seat: 13-40 or 45-50",
            "", "your ticket:", "7,1,14", "", "nearby tickets:", "7,3,47",
            "40,4,50", "55,2,20", "38,6,12"]
    test2 = ["class: 0-1 or 4-19","row: 0-5 or 8-19", "seat: 0-13 or 16-19",
             "", "your ticket:", "11,12,13", "", "nearby tickets:", "3,9,18",
             "15,1,5", "5,14,9"]
    print('Part one', run_pt1(test))
    print('Part two', run_pt2(test2))
    print(' END TEST '.center(80,'-'))

    print(' BEGIN REAL '.center(80,'-'))
    with open('day16_input', 'r') as f:
        data = [ line.strip() for line in f.readlines()]
        print('Part one', run_pt1(data))
        print('Part two', run_pt2(data))
    print(' END REAL '.center(80,'-'))
