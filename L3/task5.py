import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

min_num = MIN_ITEM
for i in range(SIZE):
    if array[i] < 0 and abs(array[i]) < abs(min_num):
        min_num = array[i]

print(min_num)