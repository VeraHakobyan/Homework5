s = input()
n = int(input())

if n > 0:
    print(s * n)
elif n < 0 and len(s) % abs(n) == 0:
    lst = [s[i:i+(len(s)//abs(n))] for i in range(0, len(s), len(s)//abs(n))]
    Sk = False
    if len(lst) == 1:
        Sk = True
    for i in range(len(lst)-1):
        if lst[i] == lst[i + 1]:
            Sk = True
        else:
            Sk = False
            break
    if Sk:
        print(lst[0])
    else:
        print('undefined')
