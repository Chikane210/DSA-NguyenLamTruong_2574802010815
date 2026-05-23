def find_name(name_arr, key_name):
    for i in range(len(name_arr)):
        if name_arr[i] == key_name:
            return i
    return -1

try:
    arr = [x for x in input().split()]
    name = input().title()
    if len(arr) == 0:
        print('Mang trong')
    else:
        print(find_name(arr, name))
except Exception as e:
    print(['error', e])