def whatFlavors(cost, money):
    for i in range(len(cost)-1):
        for j in range(i + 1, len(cost)):
            if cost[i] + cost[j] == money:
                return i+1, j+1


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        money = int(input())
        n = int(input())
        cost = []
        for _ in range(n):
            cost.append(int(input()))
        result = whatFlavors(cost, money)
        print(result)
