MIN_ITEM = 2
MAX_ITEM = 100

array = [i for i in range(MIN_ITEM, MAX_ITEM)]

for i in range (2, 10):
    count = 0
    for a in array:
        if a % i == 0:
            count += 1
    print(f'На {i} делятся {count} чисел.')
