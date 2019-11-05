import hashlib

s = input('Введите строку: ')


def substrings_counter(s):
    inter_list = []
    ind2del = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s[i:j] != ' ' and s[i:j] != s:
                inter_list.append(s[i:j])
    for i in range(len(inter_list) - 1):
        for j in range(i + 1, len(inter_list)):
            if hashlib.sha1(inter_list[i].encode('utf-8')).hexdigest() == hashlib.sha1(
                    inter_list[j].encode('utf-8')).hexdigest():
                ind2del.append(i)
    for i in sorted(ind2del, reverse=True):
        del inter_list[i]

    print(f'Сумма подстрок: {len(inter_list)}')


substrings_counter(s)
