import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

final_list = []

for i in array:
    if i % 2 == 0:
        final_list.append(array.index(i))
print(final_list)