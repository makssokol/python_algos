import sys

# Реализация номер 1

MIN_ITEM = 2
MAX_ITEM = 100

array = [i for i in range(MIN_ITEM, MAX_ITEM)]

for i in range (2, 10):
    count = 0
    for a in array:
        if a % i == 0:
            count += 1
    print(f'На {i} делятся {count} чисел.')


vars1 = [MIN_ITEM, MAX_ITEM, array, count, i, a]



# Суммарный размер занимаемой памяти: 3656 байт.

#  Реализация номер 2
array = ([i for i in range(2, 100)])
array2 = ([b for b in range(2, 10)])

for i in array2:
    count = 0
    for a in array:
        if a % i == 0:
            count += 1
    print(f'На {i} делятся {count} чисел.')

vars2 = [array, array2, count, i, a]

# Суммарный размер занимаемой памяти: 4008 байт. Ушли пара переменных, но добавился кортеж, который хранится в памяти.


# Реализация номер 3

MIN_ITEM = 2
MAX_ITEM = 100

array = [i for i in range(MIN_ITEM, MAX_ITEM)]

sum_dict = {}
for i in range (2, 10):
    count = 0
    for a in array:
        if a % i == 0:
            count += 1
    sum_dict.update({i : count})
    
    
for key in sum_dict:
    print(f'На {key} делятся {sum_dict[key]} чисел.')

vars3 = [array, sum_dict, count, i, a, key]


# Суммарный размер занимаемой памяти: 4696 байт. Хранение пар ключ-значение в словаре занимает больше памяти.


def vars_size(vars):
    total_size = 0
    for i in vars:
        iter_total_size = 0
        if hasattr(i, '__iter__'):
            iter_total_size += sys.getsizeof(i)
            if isinstance(i, dict):
                for key, value in i.items():
                    iter_total_size += sys.getsizeof(key) + sys.getsizeof(value)
            for item in i:
                iter_total_size += sys.getsizeof(item)
        total_size += iter_total_size
    print(f'Суммарный размер занимаемой памяти: {total_size} байт.')

vars_size(vars3)
