def vitri_cuoicung(arr, key):
    arr = arr[::-1]
    for i in range (len(arr)):
        if arr[i] == key:
            return len(arr) - i-1
    return -1

try:
    arr = [int(x) for x in input().split()]
    x = int(input())
    if len(arr) == 0:
        print('Mang trong')
    else:
        print(vitri_cuoicung(arr, x))
except ValueError:
    print('Dinh dang dau vao khong hop le!')