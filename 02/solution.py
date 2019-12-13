import os

PATH = os.path.dirname(os.path.realpath(__file__))

def parse_input(file="input"):
    res = []
    with open(PATH + "/" + file) as f:
        res.extend(int(n) for n in f.readline().split(','))
    return res

def process_seq(old_seq):
    seq = old_seq[:]
    for i in range(0, len(seq), 4):
        opt = seq[i]
        if opt == 99: return seq
        elif opt == 1:
            seq[seq[i+3]] = seq[seq[i+1]] + seq[seq[i+2]]
        elif opt == 2:
            seq[seq[i+3]] = seq[seq[i+1]] * seq[seq[i+2]] 
    return seq


def main():
    data = parse_input()
    data[1] = 12
    data[2] = 2
    print(data)
    print('Puzzle 1:', process_seq(data)[0])

def test():
    data1 = [1, 0, 0, 0, 99]
    data2 = [2, 3, 0, 3, 99]
    data3 = [2, 4, 4, 5, 99, 0]
    data4 = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    data = (data1, data2, data3, data4)
    for m in data:
        print(m, '=>', process_seq(m))

def test_2():
    pass

def main_2():
    data = [0]
    noun = 0
    verb = 0
    for noun in range(100):
        for verb in range(100):
            data = parse_input()
            data[1] = noun
            data[2] = verb
            if process_seq(data)[0] == 19690720: 
                print("found")
                print(noun,verb, 100*noun + verb)
                return            


if __name__ == "__main__":
    #test()
    main()
    test_2()
    main_2()
    