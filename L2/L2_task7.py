def calc(n):
    if n == 1:
        return n
    expr_left = n + calc(n - 1)
    return expr_left

n = int(input('Введите число n: '))

expr_right = int(n * (n + 1) / 2)

expr_left = calc(n)

print(f'Левая часть равенства = {expr_left}')
print(f'Правая часть равенства = {expr_right}')

if expr_left == expr_right:
    print('Равенство верно')
else:
    print('Равенсто неверно')
