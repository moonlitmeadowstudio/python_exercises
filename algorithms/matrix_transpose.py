"""
1 2 3 4       1
4 5 9 8   ->  2
0 3 1 2       3
              4
"""
def transpose(array):
    transpose_array = []
    rows = len(array)
    cols = len(array[0])
    for i in range(cols):
        sub_array = []
        for j in range(rows):
            sub_array.append(array[j][i])
        transpose_array.append(sub_array)
    return transpose_array

