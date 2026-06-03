# Bài 10. Tìm trong mảng xoay (Rotated Sorted Array)
# Mảng đã sắp xếp bị xoay tại một điểm chưa biết (không trùng). Tìm chỉ số của x.
# Ví dụ: a = [4, 5, 6, 7, 0, 1, 2], x = 0 → 4

def rotated_sorted_arr(arr, key, n):
    left = 0
    right = n -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[left] <= arr[mid]: #Kiểm tra nửa bên trái
            if key >= arr[left] and key <= arr[mid]:
                right = mid -1
            else:
                left = mid +1
        else: #Kiểm tra nửa bên phải
            if key >= arr[mid] and key <= arr[right]:
                left = mid +1
            else:
                right = mid -1
    return -1

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            x = int(input())
            if n > 0:
                rotated_arr = rotated_sorted_arr(arr, x, n)
                print(rotated_arr)
                break
            else:
                print('mang rong')
        except ValueError:
            print('Dinh dang dau vao khong hop le')