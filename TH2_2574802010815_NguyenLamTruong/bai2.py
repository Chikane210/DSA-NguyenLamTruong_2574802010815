# Bài 2. Kiểm tra tồn tại
# Cho mảng đã sắp xếp, trả về true/false cho biết x có trong mảng không.
# Ví dụ: a = [2, 4, 6, 8], x = 5 → false
def checking_element(arr, key, n):
    left = 0
    right = n -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            left = mid +1
        else:
            right = mid -1
    return False



if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            key = int(input())
            n = len(arr)
            if n > 0:
                arr_sort = sorted(arr)
                binary_search = checking_element(arr_sort, key, n)
                print(binary_search)
            else:
                print('mang rong')
            break
        except ValueError:
            print('Dinh dang dau vao khong hop le!')

        