#!/usr/bin/python3

def parse_boot(bootcode):
    operations = { 'acc': lambda x, acc, ip: (acc+x, ip+1),
                   'jmp': lambda x, acc, ip: (acc, ip+x),
                   'nop': lambda _, acc, ip: (acc, ip+1) }

    acc = 0
    ip = 0
    previous = set()
    history = list()

    while ip >=0 and ip < len(bootcode):
        if ip in previous:
            return False, acc, ip, history
        previous.add(ip)
        i = bootcode[ip]
        if i[0] in ('jmp', 'nop'):
            history.append(ip)
        (acc, ip) = operations[i[0]](int(i[1]), acc, ip)
    else:
        return True, acc, ip, history

def run_pt1(data):
    bootcode = [line.strip().split(' ') for line in data]
    err, acc, ip, history = parse_boot(bootcode)
    return acc

def run_pt2(data):
    bootcode = [line.strip().split(' ') for line in data]
    err, acc, ip, history = parse_boot(bootcode)

    for i in history:
        refinstr = [[i[0], i[1]]for i in bootcode]
        refinstr[i][0] = 'nop' if refinstr[i][0] == 'jmp' else 'jmp'
        err, acc, ip, _ = parse_boot(refinstr)
        if err is True:
            return acc

if __name__ == '__main__':
    print(' BEGIN TEST '.center(80,'-'))
    test = ["nop +0", "acc +1", "jmp +4",
            "acc +3", "jmp -3", "acc -99",
            "acc +1", "jmp -4", "acc +6"]
    print('Part one', run_pt1(test))
    print('Part two', run_pt2(test))
    print(' END TEST '.center(80,'-'))

    print(' BEGIN REAL '.center(80,'-'))
    with open('day8_input', 'r') as f:
        data = list(f)
        print('Part one', run_pt1(data))
        print('Part two', run_pt2(data))
    print(' END REAL '.center(80,'-'))
