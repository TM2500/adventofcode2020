#!/usr/bin/python3

def is_tree(fld):
    return True if fld == '#' else False

def get_x(x, rborder, mv ):
    x = (x + mv) % rborder
    return x

def traverse(grid_data, mv):
    rborder = len(grid_data[0].splitlines()[0])
    finish = len(grid_data)
    x = 0
    count = 0
    for i in range(0,finish, mv[1]):
        if i != 0:
            x = get_x(x, rborder, mv[0])
        if is_tree(grid_data[i][x]):
            count += 1
    return count

def run_pt2(data):
    slopes = ((3,1),(1,1),(5,1),(7,1),(1,2))

    pt2 = 1
    for s in slopes:
        pt2 = pt2 * traverse(data,s)
    return pt2

def run_pt1(data):
    return traverse(data, (3,1))

if __name__ == '__main__':
    print(' BEGIN TEST '.center(80,'-'))
    test = [
        '..##.......',
        '#...#...#..',
        '.#....#..#.',
        '..#.#...#.#',
        '.#...##..#.',
        '..#.##.....',
        '.#.#.#....#',
        '.#........#',
        '#.##...#...',
        '#...##....#',
        '.#..#...#.#'
        ]
    print('Part one', run_pt1(test))
    print('Part two', run_pt2(test))
    print(' END TEST '.center(80,'-'))

    print(' BEGIN REAL '.center(80,'-'))
    with open('day3_input', 'r') as f:
        grid = list(f)
        print('Part one', run_pt1(grid))
        print('Part two', run_pt2(grid))
    print(' END REAL '.center(80,'-'))
