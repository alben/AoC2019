def rule_one(number):
    str_num = str(number)
    dup = False
    for i in range(5):
        if str_num[i] == str_num[i+1]:
            dup = True
        elif str_num[i] > str_num[i+1]:
            return False
    return dup

def rule_two(number):
    str_num = str(number)
    dup = False
    i = 0
    while i < 5:
        if str_num[i] > str_num[i+1]:
            return False
        if str_num[i] == str_num[i+1]:
            o = i
            i +=1
            while i < 5 and str_num[i] == str_num[i+1]:
                i +=1
            if o == i-1:
                dup = True
        else:
            i += 1
    return dup

def get_candidates_one(min_num=0, max_num=999999):
    candidates = []
    for i in range(min_num, max_num + 1):
        if rule_one(i):
            candidates.append(i)
    print(len(candidates))

def get_candidates_two(min_num=0, max_num=999999):
    candidates = []
    for i in range(min_num, max_num + 1):
        if rule_two(i):
            candidates.append(i)
    print(len(candidates))

if __name__ == "__main__":
    # input 307237-769058
    get_candidates_one(307237, 769058)
    get_candidates_two(307237, 769058)