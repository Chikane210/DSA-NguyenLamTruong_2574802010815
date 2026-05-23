def ton_tai(arr, key):
    check = False
    i = 0
    while i < len(arr):
        if arr[i] == key:
            check = True
        i = i + 1
    return check

try:
    arr = [int(x) for x in input().split()]
    x = int(input())
    if len(arr) == 0:
        print('Mang trong')
    else:
        print(ton_tai(arr, x))
except ValueError:
    print('Dinh dang dau vao khong hop le!')