# Bài 4. Vị trí xuất hiện cuối cùng
# Như bài 3 nhưng tìm chỉ số lớn nhất mà a[i] = x.
# Ví dụ: a = [1, 2, 2, 2, 3], x = 2 → 3
def xuat_hien_cuoi(arr, key, n):
    left = 0
    right = n -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            i = mid
            while i < n and key ==  arr[i]:
                max_pos = i
                i +=1
            return max_pos
        elif arr[mid] > key:
            right = mid -1
        else:
            left = mid +1
    return max_pos

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            key = int(input())
            n = len(arr)
            if n > 0:
                arr_sort = sorted(arr)
                chiso_lonnhat = xuat_hien_cuoi(arr_sort, key, n)
                print(chiso_lonnhat)
            else:
                print('mang rong')
            break
        except ValueError:
            print('Dinh dang dau vao khong hop le!')