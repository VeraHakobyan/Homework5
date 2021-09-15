def twoStrings(s1, s2):
    for el1 in s1:
        for el2 in s2:
            if el1 == el2:
                return "Yes"
    return "No"


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        str1 = input()
        str2 = input()
        result = twoStrings(str1, str2)
        print(result)
