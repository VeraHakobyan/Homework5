
def beautifulBinaryString(b):
    count = 0
    i = 0
    while i < len(b):
        if b[i:i + 3] == '010':
            count += 1
            i += 3
        else:
            i += 1
    return count


n = int(input())
b = ''
for i in range(n):
    b += input()

print(beautifulBinaryString(b))
