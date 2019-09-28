x1 = float(input('Введите координату x1: '))
x2 = float(input('Введите координату x2: '))
y1 = float(input('Введите координату y1: '))
y2 = float(input('Введите координату y2: '))
k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1
print(f'Уравнение прямой: y = {k}x + {b}')
