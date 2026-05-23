def sentinel(arr,key):
    arr.append(key)
    count = i = 0
    while arr[i] != key:
        count +=1
        i = i + 1
    count +=1
    arr.pop()
    if i < len(arr):
        return i, count
    return -1, count

def LinearSearch(arr, key):
    count = i = 0
    while i < len(arr):
        count+=1
        if arr[i] == key:
            return i, count
        i = i + 1
    return -1, count

try:
    arr = [int(x) for x in input().split()]
    x = int(input())
    if len(arr) == 0:
        print('Mang trong')
    else:
        s_result, s_count = sentinel(arr,x)
        ls_result, ls_count = LinearSearch(arr,x)
        print(f'Sentinel: vi tri={s_result}, lan thuc hien={s_count}')
        print(f'LinearSearch: vi tri={ls_result}, lan thuc hien={ls_count}')
except ValueError:
    print('Dinh dang dau vao khong hop le!')