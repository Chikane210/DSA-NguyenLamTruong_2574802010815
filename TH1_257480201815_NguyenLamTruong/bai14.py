def even_number(number_arr):
    for i in range(len(number_arr)):
        if number_arr[i] % 2 ==0:
            return i
    return -1

try:
    arr = [int(x) for x in input().split()]
    if len(arr) == 0:
        print('Mang trong')
    else:
        print(even_number(arr))
except ValueError:
    print('Dinh dang dau vao khong hop le!')