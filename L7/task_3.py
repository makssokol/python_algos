from random import randint

m = int(input('Введите число m: '))

array = [randint(1, 20) for i in range(m * 2 + 1)]

print(array)

def mediana(array):

    for i in range(len(array)):
        less = []
        more = []
        eq = []
        for j in range(len(array)):
            if array[j] < array[i]:
                less.append(array[j])
            elif array[j] > array[i]:
                more.append(array[j])
            else:
                eq.append(j)
        if len(less) == len(more) or (len(eq) > 1 and abs(len(more) - len(less)) < len(eq)):
            return array[i]

print(mediana(array))