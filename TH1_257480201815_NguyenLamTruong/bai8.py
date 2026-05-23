def dem_xuat_hien(arr, key):
    dem = 0
    for i in range (len(arr)):
        if arr[i] == key:
            dem += 1
    return dem

try:
    arr = [int(x) for x in input().split()]
    x = int(input())
    if len(arr) == 0:
        print('Mang trong')
    else:
        print(dem_xuat_hien(arr, x))
except ValueError:
    print('Dinh dang dau vao khong hop le!')