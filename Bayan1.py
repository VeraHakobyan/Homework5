N = int(input("The number of stores: "))

brand_of_store = []
repeated_stores = 0

for _ in range(N):
    brand_of_store.append(input())

for i in range(len(brand_of_store)):
    for j in range(i):
        if brand_of_store[j] == brand_of_store[i]:
            repeated_stores += 1
            break

print(repeated_stores)
