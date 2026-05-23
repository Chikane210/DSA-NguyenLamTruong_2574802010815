def ktr_so_ngto(n):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                return False
    return True

def vitri_dautien(number_arr):
    for i in range (len(number_arr)):
        if ktr_so_ngto(number_arr[i])==True:
            return i
    return -1

try:
    arr = [int(x) for x in input().split()]
    if len(arr) == 0:
        print('Mang trong')
    else:
        print(vitri_dautien(arr))
except ValueError:
    print('Dinh dang dau vao khong le!')
    