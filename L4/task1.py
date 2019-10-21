# Чтобы разное расположение минимального и максимального числа не влияло на результаты сравнения работы алгоритмов,
# создадим и сохраним списки разной длины в отдельные переменные, а код по генерации списков закомментим

# import random

# SIZE = 1000
# MIN_ITEM = 0
# MAX_ITEM = 1000
# array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
import timeit
import cProfile

array10 = [56, 28, 6, 49, 4, 84, 94, 52, 84, 62]
array100 = [94, 35, 12, 42, 97, 69, 29, 65, 97, 66, 61, 24, 89, 69, 74, 97, 28, 13, 55, 72, 42, 55, 78, 82, 41, 45, 52, 43, 56, 72, 54, 11, 79, 3, 82, 50, 94, 9, 100, 5, 38, 55, 3, 11, 29, 80, 51, 63, 22, 12, 65, 71, 7, 73, 57, 90, 22, 55, 81, 80, 19, 77, 33, 23, 8, 82, 22, 69, 84, 91, 90, 38, 49, 66, 46, 55, 2, 70, 66, 39, 19, 1, 23, 59, 96, 19, 25, 1, 75, 84, 9, 98, 50, 54, 11, 63, 78, 61, 5, 26]
array1000 = [806, 795, 312, 486, 292, 743, 94, 723, 661, 884, 304, 746, 643, 871, 5, 383, 295, 368, 375, 473, 502, 747, 753, 409, 394, 587, 208, 921, 989, 515, 905, 221, 550, 181, 704, 251, 714, 312, 445, 817, 708, 970, 754, 971, 810, 527, 490, 422, 681, 289, 997, 759, 658, 657, 31, 76, 887, 165, 242, 494, 218, 268, 326, 449, 344, 121, 850, 248, 442, 35, 229, 553, 448, 717, 150, 42, 800, 867, 459, 122, 105, 35, 157, 876, 378, 725, 923, 222, 662, 168, 411, 150, 975, 902, 253, 880, 95, 584, 553, 780, 212, 447, 946, 652, 437, 939, 376, 125, 150, 663, 254, 201, 17, 103, 327, 250, 803, 957, 900, 239, 532, 118, 180, 26, 979, 832, 253, 697, 845, 269, 757, 665, 865, 284, 505, 128, 861, 682, 31, 394, 309, 750, 15, 623, 72, 780, 921, 32, 741, 322, 357, 997, 215, 671, 12, 946, 88, 487, 136, 2, 379, 900, 298, 852, 476, 648, 226, 603, 126, 903, 462, 92, 789, 311, 197, 701, 647, 532, 336, 1, 220, 621, 943, 553, 577, 867, 882, 613, 682, 856, 834, 495, 629, 228, 614, 65, 465, 249, 239, 307, 357, 224, 791, 852, 545, 292, 154, 228, 309, 152, 306, 240, 524, 980, 704, 91, 472, 657, 951, 816, 851, 301, 44, 514, 486, 849, 130, 909, 578, 936, 425, 202, 955, 607, 536, 962, 73, 455, 674, 435, 164, 190, 853, 884, 244, 532, 100, 69, 980, 500, 600, 56, 747, 909, 445, 166, 894, 236, 528, 564, 191, 747, 881, 326, 504, 348, 67, 872, 792, 523, 39, 877, 529, 198, 763, 947, 831, 590, 533, 343, 479, 799, 424, 113, 182, 139, 599, 164, 215, 626, 258, 803, 993, 117, 264, 120, 949, 785, 295, 113, 301, 339, 769, 589, 396, 299, 664, 796, 724, 680, 746, 729, 105, 379, 820, 587, 546, 822, 177, 236, 778, 646, 186, 908, 239, 519, 183, 783, 36, 929, 850, 194, 712, 708, 481, 666, 240, 198, 344, 589, 78, 345, 765, 174, 613, 402, 100, 611, 817, 736, 941, 315, 302, 159, 247, 438, 553, 295, 995, 243, 538, 742, 502, 551, 346, 70, 914, 14, 735, 548, 679, 652, 801, 626, 678, 322, 846, 992, 793, 69, 352, 844, 642, 909, 772, 23, 174, 41, 660, 271, 876, 776, 696, 191, 39, 706, 442, 391, 263, 37, 833, 85, 651, 608, 180, 385, 908, 283, 400, 804, 506, 727, 428, 645, 278, 65, 20, 978, 573, 673, 522, 30, 567, 306, 263, 508, 814, 530, 176, 360, 911, 210, 596, 612, 551, 72, 872, 399, 13, 821, 627, 833, 744, 14, 54, 272, 744, 681, 261, 842, 746, 855, 106, 313, 890, 610, 162, 545, 982, 293, 745, 315, 204, 213, 403, 281, 201, 550, 125, 214, 654, 944, 929, 100, 894, 666, 116, 460, 628, 188, 523, 838, 311, 746, 744, 138, 308, 289, 545, 311, 154, 989, 413, 949, 285, 194, 319, 792, 685, 428, 627, 278, 904, 989, 708, 317, 570, 495, 137, 712, 431, 927, 722, 194, 134, 632, 672, 337, 487, 247, 253, 178, 539, 826, 814, 607, 985, 365, 831, 958, 788, 613, 506, 380, 272, 650, 81, 779, 866, 485, 882, 607, 882, 131, 206, 820, 244, 129, 449, 792, 836, 996, 579, 146, 38, 181, 200, 141, 276, 658, 946, 298, 757, 388, 183, 316, 433, 756, 493, 303, 542, 194, 262, 418, 392, 424, 426, 527, 459, 597, 202, 472, 974, 52, 537, 122, 550, 618, 259, 133, 91, 701, 243, 28, 694, 817, 677, 232, 22, 595, 783, 221, 151, 596, 132, 446, 688, 262, 170, 334, 862, 583, 787, 390, 18, 305, 319, 269, 917, 926, 643, 85, 238, 185, 209, 821, 97, 103, 399, 497, 892, 48, 472, 171, 566, 505, 426, 842, 130, 51, 161, 80, 61, 987, 953, 723, 881, 921, 319, 649, 240, 907, 0, 594, 256, 487, 728, 403, 831, 725, 897, 589, 950, 961, 535, 686, 872, 837, 146, 619, 568, 441, 449, 935, 783, 46, 586, 138, 29, 850, 255, 499, 754, 97, 622, 657, 484, 53, 835, 704, 906, 159, 375, 310, 378, 845, 631, 393, 509, 581, 459, 922, 728, 994, 220, 851, 338, 91, 462, 67, 876, 16, 302, 744, 147, 407, 508, 696, 919, 935, 70, 427, 942, 556, 211, 896, 334, 759, 282, 52, 169, 241, 153, 296, 388, 410, 855, 344, 831, 857, 478, 378, 540, 838, 471, 856, 13, 298, 123, 976, 628, 641, 521, 153, 849, 998, 789, 674, 634, 589, 49, 246, 631, 499, 567, 157, 446, 219, 543, 930, 471, 414, 647, 541, 324, 833, 988, 713, 721, 347, 77, 828, 899, 643, 805, 212, 758, 790, 806, 204, 715, 512, 317, 762, 864, 65, 620, 892, 841, 752, 669, 256, 436, 445, 863, 998, 74, 144, 291, 186, 128, 335, 537, 479, 220, 446, 763, 900, 297, 553, 920, 654, 544, 591, 941, 646, 314, 691, 560, 705, 807, 897, 25, 759, 921, 193, 732, 735, 452, 568, 337, 164, 672, 168, 896, 876, 661, 562, 582, 105, 61, 131, 904, 265, 14, 59, 784, 568, 37, 439, 459, 130, 639, 569, 69, 316, 562, 566, 332, 51, 562, 711, 467, 749, 257, 617, 827, 107, 912, 960, 329, 278, 63, 495, 154, 469, 993, 269, 875, 508, 626, 322, 79, 634, 736, 43, 28, 519, 322, 450, 883, 107, 275, 730, 748, 132, 831, 758, 675, 89, 117, 141, 443, 535, 832, 29, 910, 130, 918, 992, 422, 386, 916, 240, 938, 886, 286, 41, 963, 963, 990, 872, 289, 356, 585, 731, 563, 254, 905, 795, 78, 650, 147, 155, 264, 933, 700, 150, 45, 270, 769, 819, 80, 99, 96, 804, 188, 50, 520, 415, 211, 188, 150, 256, 802, 603, 302, 406, 586, 88, 921, 215, 96, 233, 398, 144, 838, 577, 785, 262, 708, 27, 544, 524, 821, 511, 942, 272, 564, 97, 562, 736, 250, 496, 18, 964, 403, 164, 321, 436]


def min_max_change(a):
    min_num = a[0]
    min_ind = 0
    for i in range(len(a)):
        if a[i] < min_num:
            min_num = a[i]
            min_ind = i

    max_num = a[0]
    max_ind = 0
    for i in range(len(a)):
        if a[i] > max_num:
            max_num = a[i]
            max_ind = i

    a[min_ind] = max_num
    a[max_ind] = min_num



# cProfile.run('min_max_change(array1000)')

# print(timeit.timeit(s, number=100))
# 0.00022303900000000126 - для array10
# 0.0013560069999999994 - для array100
# 0.018461835999999995 - для array1000

# cProfile для array10
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task1.py:18(min_max_change)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile для array100
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task1.py:18(min_max_change)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile для array100
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task1.py:18(min_max_change)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def min_max_change1(a):
    index_min = 0
    index_max = 0
    for i in range(len(a)):
        if a[i] < a[index_min]:
            index_min = i
        elif a[i] > a[index_max]:
            index_max = i
    a[index_min], a[index_max] = a[index_max], a[index_min]
    return a

min_max_change1(array1000)


# print(timeit.timeit(s, number=100))
#0.00035685200000000125 - для array10
#0.0012893820000000021 - для array100
#0.019850985999999998 - для array1000

# cProfile.run('min_max_change1(array10)')
# cProfile для array10
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task1.py:67(min_max_change1)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile для array100
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task1.py:67(min_max_change1)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile для array1000
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task1.py:67(min_max_change1)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def min_max_change2(a):
    min_num = min(a)
    max_num = max(a)
    index_min = a.index(min_num)
    index_max = a.index(max_num)
    a[index_min], a[index_max] = a[index_max], a[index_min]
    return a

s = """
def min_max_change2(a):
    index_min = 0
    index_max = 0
    for i in range(len(a)):
        if a[i] < a[index_min]:
            index_min = i
        elif a[i] > a[index_max]:
            index_max = i
    a[index_min], a[index_max] = a[index_max], a[index_min]
    return a

array1000 = [806, 795, 312, 486, 292, 743, 94, 723, 661, 884, 304, 746, 643, 871, 5, 383, 295, 368, 375, 473, 502, 747, 753, 409, 394, 587, 208, 921, 989, 515, 905, 221, 550, 181, 704, 251, 714, 312, 445, 817, 708, 970, 754, 971, 810, 527, 490, 422, 681, 289, 997, 759, 658, 657, 31, 76, 887, 165, 242, 494, 218, 268, 326, 449, 344, 121, 850, 248, 442, 35, 229, 553, 448, 717, 150, 42, 800, 867, 459, 122, 105, 35, 157, 876, 378, 725, 923, 222, 662, 168, 411, 150, 975, 902, 253, 880, 95, 584, 553, 780, 212, 447, 946, 652, 437, 939, 376, 125, 150, 663, 254, 201, 17, 103, 327, 250, 803, 957, 900, 239, 532, 118, 180, 26, 979, 832, 253, 697, 845, 269, 757, 665, 865, 284, 505, 128, 861, 682, 31, 394, 309, 750, 15, 623, 72, 780, 921, 32, 741, 322, 357, 997, 215, 671, 12, 946, 88, 487, 136, 2, 379, 900, 298, 852, 476, 648, 226, 603, 126, 903, 462, 92, 789, 311, 197, 701, 647, 532, 336, 1, 220, 621, 943, 553, 577, 867, 882, 613, 682, 856, 834, 495, 629, 228, 614, 65, 465, 249, 239, 307, 357, 224, 791, 852, 545, 292, 154, 228, 309, 152, 306, 240, 524, 980, 704, 91, 472, 657, 951, 816, 851, 301, 44, 514, 486, 849, 130, 909, 578, 936, 425, 202, 955, 607, 536, 962, 73, 455, 674, 435, 164, 190, 853, 884, 244, 532, 100, 69, 980, 500, 600, 56, 747, 909, 445, 166, 894, 236, 528, 564, 191, 747, 881, 326, 504, 348, 67, 872, 792, 523, 39, 877, 529, 198, 763, 947, 831, 590, 533, 343, 479, 799, 424, 113, 182, 139, 599, 164, 215, 626, 258, 803, 993, 117, 264, 120, 949, 785, 295, 113, 301, 339, 769, 589, 396, 299, 664, 796, 724, 680, 746, 729, 105, 379, 820, 587, 546, 822, 177, 236, 778, 646, 186, 908, 239, 519, 183, 783, 36, 929, 850, 194, 712, 708, 481, 666, 240, 198, 344, 589, 78, 345, 765, 174, 613, 402, 100, 611, 817, 736, 941, 315, 302, 159, 247, 438, 553, 295, 995, 243, 538, 742, 502, 551, 346, 70, 914, 14, 735, 548, 679, 652, 801, 626, 678, 322, 846, 992, 793, 69, 352, 844, 642, 909, 772, 23, 174, 41, 660, 271, 876, 776, 696, 191, 39, 706, 442, 391, 263, 37, 833, 85, 651, 608, 180, 385, 908, 283, 400, 804, 506, 727, 428, 645, 278, 65, 20, 978, 573, 673, 522, 30, 567, 306, 263, 508, 814, 530, 176, 360, 911, 210, 596, 612, 551, 72, 872, 399, 13, 821, 627, 833, 744, 14, 54, 272, 744, 681, 261, 842, 746, 855, 106, 313, 890, 610, 162, 545, 982, 293, 745, 315, 204, 213, 403, 281, 201, 550, 125, 214, 654, 944, 929, 100, 894, 666, 116, 460, 628, 188, 523, 838, 311, 746, 744, 138, 308, 289, 545, 311, 154, 989, 413, 949, 285, 194, 319, 792, 685, 428, 627, 278, 904, 989, 708, 317, 570, 495, 137, 712, 431, 927, 722, 194, 134, 632, 672, 337, 487, 247, 253, 178, 539, 826, 814, 607, 985, 365, 831, 958, 788, 613, 506, 380, 272, 650, 81, 779, 866, 485, 882, 607, 882, 131, 206, 820, 244, 129, 449, 792, 836, 996, 579, 146, 38, 181, 200, 141, 276, 658, 946, 298, 757, 388, 183, 316, 433, 756, 493, 303, 542, 194, 262, 418, 392, 424, 426, 527, 459, 597, 202, 472, 974, 52, 537, 122, 550, 618, 259, 133, 91, 701, 243, 28, 694, 817, 677, 232, 22, 595, 783, 221, 151, 596, 132, 446, 688, 262, 170, 334, 862, 583, 787, 390, 18, 305, 319, 269, 917, 926, 643, 85, 238, 185, 209, 821, 97, 103, 399, 497, 892, 48, 472, 171, 566, 505, 426, 842, 130, 51, 161, 80, 61, 987, 953, 723, 881, 921, 319, 649, 240, 907, 0, 594, 256, 487, 728, 403, 831, 725, 897, 589, 950, 961, 535, 686, 872, 837, 146, 619, 568, 441, 449, 935, 783, 46, 586, 138, 29, 850, 255, 499, 754, 97, 622, 657, 484, 53, 835, 704, 906, 159, 375, 310, 378, 845, 631, 393, 509, 581, 459, 922, 728, 994, 220, 851, 338, 91, 462, 67, 876, 16, 302, 744, 147, 407, 508, 696, 919, 935, 70, 427, 942, 556, 211, 896, 334, 759, 282, 52, 169, 241, 153, 296, 388, 410, 855, 344, 831, 857, 478, 378, 540, 838, 471, 856, 13, 298, 123, 976, 628, 641, 521, 153, 849, 998, 789, 674, 634, 589, 49, 246, 631, 499, 567, 157, 446, 219, 543, 930, 471, 414, 647, 541, 324, 833, 988, 713, 721, 347, 77, 828, 899, 643, 805, 212, 758, 790, 806, 204, 715, 512, 317, 762, 864, 65, 620, 892, 841, 752, 669, 256, 436, 445, 863, 998, 74, 144, 291, 186, 128, 335, 537, 479, 220, 446, 763, 900, 297, 553, 920, 654, 544, 591, 941, 646, 314, 691, 560, 705, 807, 897, 25, 759, 921, 193, 732, 735, 452, 568, 337, 164, 672, 168, 896, 876, 661, 562, 582, 105, 61, 131, 904, 265, 14, 59, 784, 568, 37, 439, 459, 130, 639, 569, 69, 316, 562, 566, 332, 51, 562, 711, 467, 749, 257, 617, 827, 107, 912, 960, 329, 278, 63, 495, 154, 469, 993, 269, 875, 508, 626, 322, 79, 634, 736, 43, 28, 519, 322, 450, 883, 107, 275, 730, 748, 132, 831, 758, 675, 89, 117, 141, 443, 535, 832, 29, 910, 130, 918, 992, 422, 386, 916, 240, 938, 886, 286, 41, 963, 963, 990, 872, 289, 356, 585, 731, 563, 254, 905, 795, 78, 650, 147, 155, 264, 933, 700, 150, 45, 270, 769, 819, 80, 99, 96, 804, 188, 50, 520, 415, 211, 188, 150, 256, 802, 603, 302, 406, 586, 88, 921, 215, 96, 233, 398, 144, 838, 577, 785, 262, 708, 27, 544, 524, 821, 511, 942, 272, 564, 97, 562, 736, 250, 496, 18, 964, 403, 164, 321, 436]
min_max_change2(array1000)
"""

#print(timeit.timeit(s, number=100))
#0.00022502099999999886 - для array10
#0.001441174 - для array100
#0.018175821999999998 - для array1000

cProfile.run('min_max_change2(array1000)')
# cProfile для array10
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task1.py:122(min_max_change2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
# cProfile для array100
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task1.py:122(min_max_change2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
# cProfile для array1000
# calls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task1.py:122(min_max_change2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

"""
Выводы: приведенные три разных алгоритма перемены мест наибольшего и наименьшего элементов списка дают
примерно одинаковое время исполнения, которое увеличивается линейно с ростом длины списка. С точки зрения
количества итераций выполнения каждого действия, то все действия выполняются по одному разу, кроме
вызова функции index в последнем алгоритме, которая производит обмен переменными.
"""
