"""
Для обоих алгоритмов будем выбирать простые числа до 1000 и измерять время для поиска
50го, 100го и 150го простого числа
"""

import timeit
import cProfile

s= """
def eratosthenes(a):
    n = 1000
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]

    return res[a - 1]

eratosthenes(150)
"""

#0.040328339 - для 50го простого числа
#0.038230993 - для 100го простого числа
#0.039902635 - для 1000го простого числа


#print(timeit.timeit(s, number=100))

def eratosthenes(a):
    n = 1000
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]

    return res[a - 1]

#eratosthenes(50)

#cProfile.run('eratosthenes(100)')
#cProfile для всех значений будет таким
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task2.py:36(eratosthenes)
#         1    0.000    0.000    0.000    0.000 task2.py:38(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task2.py:48(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


t = """
def not_eratosthenes(a):
    n = 1000
    not_sieve = [i for i in range(n+1)]
    list_to_remove = []
    
    for i in not_sieve:
        for j in range(2, i // 2 + 1):
            if i % j == 0 and i in not_sieve:
                if i not in list_to_remove:
                    list_to_remove.append(i)
            j += 1
    res = [i for i in not_sieve if i not in list_to_remove and i != 0]
    return res[a - 1]
    
not_eratosthenes(150)
"""

#print(timeit.timeit(t, number=100))
#8.500157702 - для 50го простого числа
#8.517754186 - для 100го простого числа
#8.637680202 - для 150го числа

def not_eratosthenes(a):
    n = 1000
    not_sieve = [i for i in range(n+1)]
    list_to_remove = []
    
    for i in not_sieve:
        for j in range(2, i // 2 + 1):
            if i % j == 0 and i in not_sieve:
                if i not in list_to_remove:
                    list_to_remove.append(i)
            j += 1
    res = [i for i in not_sieve if i not in list_to_remove and i != 0]
    return res[a - 1]
    


cProfile.run('not_eratosthenes(100)')
# cProfile для всех значений будет таким:
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.112    0.112 <string>:1(<module>)
#         1    0.104    0.104    0.112    0.112 task2.py:88(not_eratosthenes)
#         1    0.000    0.000    0.000    0.000 task2.py:90(<listcomp>)
#         1    0.007    0.007    0.007    0.007 task2.py:99(<listcomp>)
#         1    0.000    0.000    0.112    0.112 {built-in method builtins.exec}
#       831    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


"""
Выводы: поиск простого числа по его номеру с использованием решета Эратосфена работает существенно быстрее, чем
такой же поиск с проверкой деления всех значений списка, составления списка "непростых" чисел и удаления второго списка из первого.
Разница в скорости работы составляет примерно 212 раз. Скорость работы обоих алгоритмов не зависит от порядкового номера искомого
простого числа, а зависит от длины списка, из которого мы выбираем простые числа. Слабым звеном во втором алгоритме является
метод append, который вызывается 831 раз в ходе выполнения алгоритма и это количество так же не зависит от номера искомого числа.
"""

