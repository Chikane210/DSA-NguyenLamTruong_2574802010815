# Bài 7. Upper Bound
# Tìm phần tử nhỏ nhất > x và trả về chỉ số (hoặc n nếu không có).
# Ví dụ: a = [1, 3, 5, 7], x = 5 → 3 (vì a[3] = 7)

def upper_bound(arr,key,n):
    left = 0
    right = n -1
    result = n
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= key:
            left = mid +1
        else:
            result = mid
            right = mid -1
    return result

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            key = int(input())
            n = len(arr)
            if n > 0:
                arr_sort = sorted(arr)
                upperBound = upper_bound (arr_sort, key, n)
                print(upperBound)
                break
            else:
                print('mang rong')
        except ValueError:
            print('Dinh dang dau vao khong hop le!')