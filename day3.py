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

if __name__ == '__main__':
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
    print(' BEGIN TEST '.center(80,'-'))
    t11 = traverse(test,(3,1))
    t21 = traverse(test,(1,1))
    t22 = t11
    t23 = traverse(test,(5,1))
    t24 = traverse(test,(7,1))
    t25 = traverse(test,(1,2))

    print('Part one', t11)
    tp2 = t21 * t22 * t23 * t24 * t25
    print('Part two', tp2)
    print(' END TEST '.center(80,'-'))

    print(' BEGIN REAL '.center(80,'-'))
    with open('day3_input', 'r') as f:
        grid = list(f)
        c11 = traverse(grid, (3,1))
        c21 = traverse(grid,(1,1))
        c22 = c11
        c23 = traverse(grid,(5,1))
        c24 = traverse(grid,(7,1))
        c25 = traverse(grid,(1,2))
        print('Part one', c11)
        cp2 = c21 * c22 * c23 * c24 * c25
        print('Part two', cp2)
    print(' END REAL '.center(80,'-'))
