#!/usr/bin/python3
def is_valid_pt1(min_occ, max_occ, char, passwd):
    if passwd.count(char) in range(min_occ, max_occ + 1):
        return True
    return False

def is_valid_pt2(idx1, idx2, char, passwd):
    idx1 = idx1 - 1
    idx2 = idx2 - 1

    if passwd[idx1] == passwd[idx2]:
        return False
    if passwd[idx1] == char: return True;
    if passwd[idx2] == char: return True;
    return False

def parseline(line):
    args = line.split()
    (min_occ, max_occ) = args[0].split('-')
    return int(min_occ), int(max_occ), args[1][0], args[2]

def count_valid(data, func):
    valid = 0
    for line in data:
        (min_occ, max_occ, char, passwd) = parseline(line)
        if func(min_occ, max_occ, char, passwd):
            valid += 1
        else:
            continue
    return valid

if __name__ == '__main__':
    test = ['1-3 a: abcde','1-3 b: cdefg','2-9 c: ccccccccc']
    print(count_valid(test, is_valid_pt1))
    print(count_valid(test, is_valid_pt2))

    with open('day2_input','r') as f:
        data = list(f)
        print(count_valid(data, is_valid_pt1))
        print(count_valid(data, is_valid_pt2))
