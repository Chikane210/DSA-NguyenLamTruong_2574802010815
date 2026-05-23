def matran(arr, key):
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] == key:
                return row, col
    return -1,-1

matrix_ = []
try:
    rows = int(input('row: '))
    for i in range(rows):
        col = [int(x) for x in input().split()]
        if len(col) == 0:
            print('Mang rong')
        matrix_.append(col)
    x = int(input())
    print(matran(matrix_,x))
except ValueError:
    print('Dinh dang dau vao khong hop le!')

