from collections import deque

a = input('Введите первое число в 16ричной системе: ')
b = input('Введите второе число в 16ричной системе: ')

a_hex_deque = deque(a.upper())
b_hex_deque = deque(b.upper())

hex_syst = {'0': '0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', 'A':'10',
 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}

hex_tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')


def hex_sum(a_hex_deque, b_hex_deque):
    if len(a_hex_deque) > len(b_hex_deque):
        for i in range(len(a_hex_deque) - len(b_hex_deque)):
            b_hex_deque.appendleft('0')
    else:
        for i in range(len(b_hex_deque) - len(a_hex_deque)):
            a_hex_deque.appendleft('0')

    ostatok = 0

    sum_hex = deque()

    for i in range(len(a_hex_deque)):
        num = int(hex_syst[a_hex_deque.pop()]) + int(hex_syst[b_hex_deque.pop()]) + ostatok
        if num >= 16:
            ostatok = num // 16
            num = num % 16
        else:
            ostatok = 0
        sum_hex.appendleft(hex_tuple[num])

    if ostatok > 0:
        sum_hex.appendleft(ostatok)
        
    return str(sum_hex)


print(f'Сумма введенных чисел равна {hex_sum(a_hex_deque, b_hex_deque)}.')