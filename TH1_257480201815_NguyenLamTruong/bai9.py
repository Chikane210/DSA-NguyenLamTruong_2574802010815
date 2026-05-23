def tim_tat_ca(arr, key):
    result = []
    for i in range (len(arr)):
        if arr[i] == key:
            result.append(i)
    return result

try:
    arr = [int(x) for x in input().split()]
    x = int(input())
    if len(arr) == 0:
        print('Mang trong')
    else:
        print(tim_tat_ca(arr, x))
except ValueError:
    print('Dinh dang dau vao khong hop le!')