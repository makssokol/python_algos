# ссылка на диаграммы https://drive.google.com/file/d/1A1xXQRFNA52vUD62Z1i_0GAU7mMYkTWp/view?usp=sharing


a = int(input('Введите трехзначное число: '))
b = a // 100
c = (a - b * 100) // 10
d = a - b * 100 - c * 10
x = b * c * d
y = b + c + d
print(f'Сумма цифр равна {y}, произведение равно {x}')
