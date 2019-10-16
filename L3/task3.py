import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

min_num = array[0]
min_ind = 0
for i in range(SIZE):
    if array[i] < min_num:
        min_num = array[i]
        min_ind = i

max_num = array[0]
max_ind = 0
for i in range(SIZE):
    if array[i] > max_num:
        max_num = array[i]
        max_ind = i

print(max_num)
print(min_num)

array[min_ind] = max_num
array[max_ind] = min_num

print(array)