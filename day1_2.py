#!/usr/bin/python3

def find_entries(entries):
    l = len(entries)
    for i in range(l):
        ei = int(entries[i])
        print(ei)
        for j in range(i+1,l):
            ej = int(entries[j])
            print(ej)
            for k in range(i+3,l):
                ek = int(entries[k])
                if ei + ej + ek == 2020:
                    print("Factors:", ei, ",", ej, ",", ek)
                    return ei * ej * ek

def __main__():
    print("Test")
    test = [1721, 979, 366, 299, 675, 1455]
    result = find_entries(test)
    print("Testesult:",result)

    entries = []
    with open('day1_input', 'r') as f:
        entries = list(f)

    result = find_entries(entries)
    print("Result:",result)

if __name__ == '__main__':
    __main__()
