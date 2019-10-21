import random

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

# Строим новый список с частотой находящихся в первом списке элементов

new_array = []

for i in array:
    count = 0
    for a in range(SIZE):
        if i == array[a]:
            count += 1
    new_array.append(count)

# Ищем максимальные и минимальные значения и их индексы в новом списке

min_num = new_array[0]
min_ind = 0
for i in range(SIZE):
    if new_array[i] < min_num:
        min_num = new_array[i]
        min_ind = i

max_num = new_array[0]
max_ind = 0
for i in range(SIZE):
    if new_array[i] > max_num:
        max_num = new_array[i]
        max_ind = i

# Ищем значения из первого списка по индексам из второго списка

max_freq_num = array[max_ind]
min_freq_num = array[min_ind]

print(f'Чаще всего встречается число {max_freq_num}')
print(f'Реже всего встречается число {min_freq_num}')
