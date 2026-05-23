def min_max(arr):
    min_value = arr[0]
    max_value = arr[0]
    for i in range (len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
        if arr[i] < min_value:
            min_value = arr[i]
    return max_value, min_value

try:
    arr = [int(x) for x in input().split()]
    if len(arr) == 0:
        print('Mang trong')
    else:
        max_value, min_value = min_max(arr)
        print(min_value)
        print(max_value)
except ValueError:
    print('Dinh dang dau vao khong hop le!')