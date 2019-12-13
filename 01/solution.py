import os

PATH = os.path.dirname(os.path.realpath(__file__))

def parse_input(file="input"):
    res = []
    with open(PATH + "/" + file) as f:
        res.extend((int(l) for l in f.readlines()))
    return res

def calc_fuel(mass):
    return mass//3 - 2

def calc_fuel_2(mass):
    total = 0
    while(True):
        mass = calc_fuel(mass)
        if mass < 0: break
        total += mass
    return total

def main():
    lines = parse_input()
    print(sum((calc_fuel(m) for m in lines)))

def test():
    lines = (12, 14, 1969, 100756)
    for m in lines:
        print(m, calc_fuel(m))

def test_2():
    lines = (12, 14, 1969, 100756)
    for m in lines:
        print(m, calc_fuel_2(m))

def main_2():
    lines = parse_input()
    print(sum((calc_fuel_2(m) for m in lines)))

if __name__ == "__main__":
    test()
    main()
    test_2()
    main_2()
    