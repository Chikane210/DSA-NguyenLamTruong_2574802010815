def ptu_lonnhat(arr):
    key = arr[0]
    for i in range(len(arr)):
        if arr[i] > key:
            key = arr[i]
    return key

try:
    arr = [int(x) for x in input().split()]
    if len(arr) == 0:
        print('Mang trong')
    else:
        print(ptu_lonnhat(arr))
except ValueError:
    print('Dinh dang dau vao khong hop le!')