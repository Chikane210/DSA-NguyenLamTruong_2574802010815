def linearsearch(arr, key):
    i = 0
    while i < len(arr):
        if arr[i] == key:
            return i
        i = i + 1
    return -1

try:
    arr = [int(x) for x in input().split()]
    x = int(input())
    if len(arr) == 0:
        print('Mang trong')
    else:
        print(linearsearch(arr, x))
except ValueError:
    print('Dinh dang dau vao khong hop le!')