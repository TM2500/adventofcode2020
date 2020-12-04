#!/usr/bin/python3

import re

def run_pt2(data):
    valid = 0
    fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    for line in data:
        if all(fld in line for fld in fields):
            byr = re.search('byr:([^ \n]+)', line).groups()[0]
            iyr = re.search('iyr:([^ \n]+)', line).groups()[0]
            eyr = re.search('eyr:([^ \n]+)', line).groups()[0]
            hgt = re.search('hgt:([^ \n]+)', line).groups()[0]
            hcl = re.search('hcl:([^ \n]+)', line).groups()[0]
            ecl = re.search('ecl:([^ \n]+)', line).groups()[0]
            pid = re.search('pid:([^ \n]+)', line).groups()[0]

            valid += \
                re.match('^[0-9]{4}$', byr) != None and 1920 <= int(byr) <= 2002 and \
                re.match('^[0-9]{4}$', iyr) != None and 2010 <= int(iyr) <= 2020 and \
                re.match('^[0-9]{4}$', eyr) != None and 2020 <= int(eyr) <= 2030 and \
                re.match('^((1([5-8][0-9]|9[0-3]))cm|(59|6[0-9]|7[0-6])in)$', hgt) != None and \
                re.match('^#[0-9a-z]{6}$', hcl) != None and \
                re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', ecl) != None and \
                re.match('^[0-9]{9}$', pid) != None
    return valid

def run_pt1(data):
    valid = 0;
    fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    for el in data:
        valid += all(fld in el for fld in fields)
    return valid

if __name__ == '__main__':
    print(' BEGIN TEST '.center(80,'-'))
    with open('day4_sample','r') as s:
        test = [x for x in s.read().split("\n\n") if x]
        print('Part one', run_pt1(test))
        print('Part two', run_pt2(test))
    print(' END TEST '.center(80,'-'))

    print(' BEGIN REAL '.center(80,'-'))
    with open('day4_input', 'r') as f:
        grid = [x for x in f.read().split("\n\n") if x]
        print('Part one', run_pt1(grid))
        print('Part two', run_pt2(grid))
    print(' END REAL '.center(80,'-'))
