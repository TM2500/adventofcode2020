#!/usr/bin/python3

from itertools import product
from collections import defaultdict


def parse_data(data):
    # spots
    rows, cols = len(data), len(data[0])
    spots = set(product(range(rows), range(cols)))

    # seats
    seats = set()
    for r, line in enumerate(data):
        for c, symbol in enumerate(line):
            if symbol == 'L':
                seats.add((r, c))

    # adjacent seats: part 1
    ad_seats = dict()
    for seat in seats:
        ad_seats[seat] = \
            (set(product(range(seat[0]-1, seat[0]+2), range(seat[1]-1, seat[1]+2))) - {seat}).intersection(spots)

    # visible seats: part 2
    vis_seats = defaultdict(set)
    directions = set(product(range(-1, 2), range(-1, 2))) - {(0, 0)}
    for seat in seats:
        for direction in directions:
            multiplier = 1
            while (trial_seat := (seat[0] + multiplier * direction[0], seat[1] + multiplier * direction[1])) in spots:
                if trial_seat in seats:
                    vis_seats[seat].add(trial_seat)
                    break
                else:
                    multiplier += 1

    return seats, ad_seats, vis_seats


def part1(seats, adjacent_seats, visible_seats, p1=True):
    occupied_seats = set()
    while True:
        occupy_next_round = set()
        for seat in seats:
            if p1:
                n_occupied_around = len(adjacent_seats[seat].intersection(occupied_seats))
            else:
                n_occupied_around = len(visible_seats[seat].intersection(occupied_seats))

            if seat not in occupied_seats and n_occupied_around == 0:
                occupy_next_round.add(seat)
            elif seat in occupied_seats and n_occupied_around < (4 if p1 else 5):
                occupy_next_round.add(seat)

        if occupied_seats == occupy_next_round:
            return len(occupied_seats)

        occupied_seats = occupy_next_round.copy()



def run_pt1(data):
    seats, ad_seats, vis_seats = parse_data(data)
    return part1(seats, ad_seats, vis_seats)

def run_pt2(data):
    seats, ad_seats, vis_seats = parse_data(data)
    return part1(seats, ad_seats, vis_seats, p1=False)

if __name__ == '__main__':
    print(' BEGIN TEST '.center(80,'-'))
    test = ["L.LL.LL.LL",
            "LLLLLLL.LL",
            "L.L.L..L..",
            "LLLL.LL.LL",
            "L.LL.LL.LL",
            "L.LLLLL.LL",
            "..L.L.....",
            "LLLLLLLLLL",
            "L.LLLLLL.L",
            "L.LLLLL.LL"]
    print('Part one', run_pt1(test))
    print('Part two', run_pt2(test))
    print(' END TEST '.center(80,'-'))

    print(' BEGIN REAL '.center(80,'-'))
    with open('day11_input', 'r') as f:
        data = list(f)
        print('Part one', run_pt1(data))
        print('Part two', run_pt2(data))
    print(' END REAL '.center(80,'-'))
