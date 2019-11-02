from random import uniform

array = [round(uniform(0, 49.9), 1) for i in range(10)]

print(array)

def merge_sort(array):
    left = []
    right = []
    if len(array) <= 1:
        return array
    else:
        mid_idx = len(array) // 2
        for i in array[0:mid_idx]:
            left.append(i)
        for j in array[mid_idx:len(array)]:
            right.append(j)
        left = merge_sort(left)
        right = merge_sort(right)
        final = merge(left, right)
        return final

def merge(left, right):
    final = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            final.append(left[0])
            left.pop(0)
        else:
            final.append(right[0])
            right.pop(0)
    while len(left) > 0:
        final.append(left[0])
        left.pop(0)
    while len(right):
        final.append(right[0])
        right.pop(0)
    return final


print(merge_sort(array))