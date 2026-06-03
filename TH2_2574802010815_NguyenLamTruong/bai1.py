# Bài 1. Tìm kiếm cơ bản
# Cho mảng a đã sắp xếp tăng dần và số x. Trả về chỉ số của x trong mảng, hoặc -1 nếu không
# có.
# Ví dụ: a = [1, 3, 5, 7, 9], x = 7 → 3
def binarySearch(arr,key,n):
    left = 0
    right = n -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
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
                binary_search = binarySearch(arr_sort, key, n)
                if binary_search == -1:
                    print('Khong tim thay phan tu trong mang')
                else:
                    print(binary_search)
                    break
            else:
                print('mang rong')
        except ValueError:
            print('Dinh dang dau vao khong hop le!')