#!/usr/bin/python3

import re

class n:
  def __init__(self,value):
    self.value = value
  def __mul__(self,other):
    return n(self.value * other.value)
  def __pow__(self,other):
    return n(self.value + other.value)
  def __matmul__(self,other):
    return n(self.value + other.value)
  def __repr__(self):
    return f'n({self.value})'

def sum_(st):
  v = re.sub(r'(\d+)', r'n(\1)', st).replace('+','@')
  return eval(v).value

def advanced(st):
  v = re.sub(r'(\d+)', r'n(\1)', st).replace('+','**')
  return eval(v).value

def run_pt1(data):
    val = 0
    for line in data:
        val += sum_(line)
    return val

def run_pt2(data):
    val = 0
    for line in data:
        val += advanced(line)
    return val

if __name__ == '__main__':
    print(' BEGIN TEST '.center(80,'-'))
    test = ["2 * 3 + (4 * 5)", "5 + (8 * 3 + 9 + 3 * 4 * 3)",
            "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
            "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]
    test2 = ["1 + (2 * 3) + (4 * (5 + 6))"]
    print('Part one', run_pt1(test))
    print('Part two', run_pt2(test2))
    print(' END TEST '.center(80,'-'))

    print(' BEGIN REAL '.center(80,'-'))
    with open('day18_input', 'r') as f:
        data = list(f)
        print('Part one', run_pt1(data))
        print('Part two', run_pt2(data))
    print(' END REAL '.center(80,'-'))
