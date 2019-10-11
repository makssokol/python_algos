a = input('Введите натуральное число: ')

even = 0
odd = 0

for i in a:
    if int(a) % 2 == 0:
        even += 1
    else:
        odd +=1
    a = int(a) // 10

print(f'Количество четных цифр: {even}. Количество нечетных цифр: {odd}.')
