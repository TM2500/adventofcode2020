#!/usr/bin/python3

import re
import functools

def split_input(data):
    idx = data.index('')
    return data[:idx], data[idx+1:]

def build_regexp(rules, value, max_depth, depth):
    if isinstance(value, str):
        return value

    if depth == max_depth:
        return ''

    return (
        '(' + '|'.join(
            ''.join(
                build_regexp(rules, rules[num], max_depth, depth+1)
                for num in part
            ) for part in value
        ) + ')'
    )

def parse_rules(data, max_depth=-1):
    rules = {
        int(halves[0]): (
            halves[1].split('"')[1].split('"')[0]
            if '"' in halves[1] else
            [list(map(int, part.split(' '))) for part in halves[1].split(' | ')]
        ) for line in data if (halves := line.split(': '))
    }

    return build_regexp(rules, rules[0], max_depth, 0)

def run_pt1(data):
    rules, messages = split_input(data)
    regexp = parse_rules(rules)
    return sum(bool(re.fullmatch(regexp, message)) for message in messages)

def run_pt2(data):
    rules, messages = split_input(data)
    longest_rule = functools.reduce(
        lambda a, b: a if a > b else b, map(len, messages), 0)
    rules[rules.index("8: 42")] = "8: 42 | 42 8"
    rules[rules.index("11: 42 31")] = "11: 42 31 | 42 11 31"
    regexp = parse_rules(rules, longest_rule)
    return sum(bool(re.fullmatch(regexp, message)) for message in messages)

if __name__ == '__main__':
    print(' BEGIN TEST '.center(80,'-'))
    test = ["0: 4 1 5","1: 2 3 | 3 2", "2: 4 4 | 5 5", "3: 4 5 | 5 4", '4: "a"',
            '5: "b"', "", "ababbb", "bababa", "abbbab", "aaabbb", "aaaabbb"]
    test2 = ["42: 9 14 | 10 1", "9: 14 27 | 1 26", "10: 23 14 | 28 1",
             '1: "a"', "11: 42 31", "5: 1 14 | 15 1", "19: 14 1 | 14 14",
             "12: 24 14 | 19 1", "16: 15 1 | 14 14", "31: 14 17 | 1 13",
             "6: 14 14 | 1 14", "2: 1 24 | 14 4", "0: 8 11", "13: 14 3 | 1 12",
             "15: 1 | 14", "17: 14 2 | 1 7", "23: 25 1 | 22 14", "28: 16 1",
             "4: 1 1", "20: 14 14 | 1 15", "3: 5 14 | 16 1", "27: 1 6 | 14 18",
             '14: "b"', "21: 14 1 | 1 14", "25: 1 1 | 1 14", "22: 14 14",
             "8: 42", "26: 14 22 | 1 20", "18: 15 15", "7: 14 5 | 1 21",
             "24: 14 1", "", "abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa",
             "bbabbbbaabaabba", "babbbbaabbbbbabbbbbbaabaaabaaa",
             "aaabbbbbbaaaabaababaabababbabaaabbababababaaa",
             "bbbbbbbaaaabbbbaaabbabaaa", "bbbababbbbaaaaaaaabbababaaababaabab",
             "ababaaaaaabaaab", "ababaaaaabbbaba", "baabbaaaabbaaaababbaababb",
             "abbbbabbbbaaaababbbbbbaaaababb", "aaaaabbaabaaaaababaa",
             "aaaabbaaaabbaaa", "aaaabbaabbaaaaaaabbbabbbaaabbaabaaa",
             "babaaabbbaaabaababbaabababaaab",
             "aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"]
    print('Part one', run_pt1(test))
    print('Part two', run_pt2(test2))
    print(' END TEST '.center(80,'-'))

    print(' BEGIN REAL '.center(80,'-'))
    with open('day19_input', 'r') as f:
        data = [line.strip() for line in list(f)]
        print('Part one', run_pt1(data))
        print('Part two', run_pt2(data))
    print(' END REAL '.center(80,'-'))
