# Bài 3. Vị trí xuất hiện đầu tiên
# Mảng đã sắp xếp có phần tử trùng. Tìm chỉ số nhỏ nhất mà a[i] = x.
# Ví dụ: a = [1, 2, 2, 2, 3], x = 2 → 1

def xuat_hien_dau(arr, key, n):
    left = 0
    right = n -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            i = mid
            while i >= 0 and key == arr[i]:
                min_pos = i
                i -=1
            return min_pos
        elif arr[mid] > key:
            right = mid -1
        else:
            left = mid +1
    return -1
    
if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            key = int(input())
            n = len(arr)
            if n > 0:
                arr_sort = sorted(arr)
                chiso_nhonhat = xuat_hien_dau(arr_sort, key, n)
                print(chiso_nhonhat)
            else:
                print('mang rong')
            break
        except ValueError:
            print('Dinh dang dau vao khong hop le!')