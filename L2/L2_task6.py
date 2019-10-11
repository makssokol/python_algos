import random

a = random.randint(0, 100)

for i in range(1,11):
    num = int(input('Угадайте загаданное число от 0 до 100. Введите число: '))
    if num == a:
        print('Поздравляю! Вы угадали.')
        break
    elif a > num:
        print('Ваше число меньше загаданного. Попробуйте еще раз.')
    elif a < num:
        print('Ваше число больше загаданного. Попробуйте еще раз.')
   
if num != a:
    print('Вы не угадали за 10 попыток.')
