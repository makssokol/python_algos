
while True:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    znak = input('Введите знак: ')

    if znak == '0':
        break
        
    if b == 0 and znak == '/':
        print('На ноль делить нельзя')
    elif znak != '+' and znak != '-' and znak != '/' and znak != '*':
        print('Введен неверный знак. Попробуйте еще раз.')
    else:
        if znak == '+':
            x = a + b
        elif znak == '-':
            x = a - b
        elif znak == '*':
            x = a * b
        else:
            x = a / b
        print(f'Результат равен {x}.')
