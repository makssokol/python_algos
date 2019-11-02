from random import randint

array = [randint(-100, 99) for i in range(10)]


def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1

bubble_sort(array)
print(array)