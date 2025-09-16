from algorithms import bubble_sort
from algorithms import transpose
from algorithms import  mirror_matrix

print(bubble_sort([2, 3, 1, 5, 44, 22, 12]))

list = [[1, 2, 3, 4],
        [4, 5, 9, 8],
        [0, 3, 1, 2]]

print(transpose(list))

l = [
    [11, 12, 13, 14, 15, 16],
    [21, 22, 23, 24, 25, 26],
    [31, 32, 33, 34, 35, 36],
    [41, 42, 43, 44, 45, 46],
    [51, 52, 53, 54, 55, 56],
    [61, 62, 63, 64, 65, 66],
]

print(mirror_matrix(l))