import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# находим первое минимальное число
min_num = array[0]
for i in range(SIZE):
    if array[i] < min_num:
        min_num = array[i]

# находим второе минимальное число
min_num2 = array[0]
for i in array:
    if i != min_num and i < min_num2:
        min_num2 = array[i]
    elif i == min_num:
        min_num2 = min_num
    else:
        pass

print(f'Первое минимальное число: {min_num}. Второе минимальное число: {min_num2}')
