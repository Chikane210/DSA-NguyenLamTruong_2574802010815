# Bài 9. Vị trí chèn (Search Insert Position)
# Mảng đã sắp xếp không trùng. Trả về chỉ số mà x nên được chèn vào để giữ thứ tự.
# Ví dụ: a = [1, 3, 5, 6], x = 4 → 2

def vitri_chen(arr, key, n):
    left = 0
    right = n -1
    result = n
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= key:
            result = mid
            right = mid -1
        elif arr[mid] < key:
            left = mid +1
    return result

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            x = int(input())
            if n > 0:
                arr_sort = sorted(arr)
                insert_pos = vitri_chen(arr, x, n)
                print(insert_pos)
                break
            else:
                print('mang rong')
        except ValueError:
            print('Dinh dang dau vao khong hop le')