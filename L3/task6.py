import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# ищем минимальное число и его индекс
min_num = array[0]
min_ind = 0
for i in range(SIZE):
    if array[i] < min_num:
        min_num = array[i]
        min_ind = i

# ищем максимальное число и его индекс
max_num = array[0]
max_ind = 0
for i in range(SIZE):
    if array[i] > max_num:
        max_num = array[i]
        max_ind = i

# складываем числа между минимальным и максимальным числами, если минимальное левее, 
# или между максимальным и минимальным числами, если максимальное левее
sum_ = 0
if min_ind < max_ind:
    for i in array[min_ind + 1:max_ind]:
        sum_ = sum_ + i
else:
    for i in array[max_ind + 1:min_ind]:
        sum_ = sum_ + i
print(f'Сумма между минимальным и максимальным элементами равна {sum_}')