def stone_in_jewels(str_jewels, str_stones):
    number_of_stone = 0
    for stone in str_stones:
        for jewel in str_jewels:
            if stone == jewel:
                number_of_stone += 1
    return number_of_stone


jewels = input('Jewels: ')
stones = input('Stones: ')

result = stone_in_jewels(jewels, stones)
print(result)
