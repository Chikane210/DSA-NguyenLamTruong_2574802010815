# Đếm số lần x xuất hiện trong mảng đã sắp xếp.
# Ví dụ: a = [1, 2, 2, 2, 3], x = 2 → 3

def min_pos(arr,key,n):
    left = 0
    right = n -1
    while left <=  right:
        mid = (left + right) //2
        if arr[mid] == key:
            i = mid
            while i >= 0 and arr[i] == key:
                min_pos = i
                i -= 1
            return min_pos
        elif arr[mid]  > key:
            right = mid -1
        else:
            left = mid +1
    return -1

def max_pos(arr,key,n):
    left = 0
    right = n -1
    while left <=  right:
        mid = (left + right) //2
        if arr[mid] == key:
            i = mid
            while i <= n and arr[i] == key:
                max_pos = i
                i += 1
            return max_pos
        elif arr[mid]  > key:
            right = mid -1
        else:
            left = mid +1
    return -1

def dem_x(arr,key,n):
    chiso_nhonhat = min_pos(arr,key,n)
    chiso_lonnhat = max_pos(arr,key,n)
    if chiso_lonnhat != -1 and chiso_nhonhat != -1:
        dem = (chiso_lonnhat - chiso_nhonhat) + 1
    else:
        dem = 0
    return dem

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            key = int(input())
            n = len(arr)
            if n > 0:
                arr_sort = sorted(arr)
                lan_xuat_hien = dem_x(arr_sort, key, n)
                print(lan_xuat_hien)
            else:
                print('mang rong')
            break
        except ValueError:
            print('Dinh dang dau vao khong hop le!')  

