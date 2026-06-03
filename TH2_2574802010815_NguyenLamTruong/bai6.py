# Bài 6. Lower Bound
# Tìm phần tử nhỏ nhất ≥ x và trả về chỉ số của nó (hoặc n nếu không có).
# Ví dụ: a = [1, 3, 5, 7], x = 4 → 2 (vì a[2] = 5)

def lower_bound(arr,key,n):
    left = 0
    right  = n -1
    result = n
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
           result = mid
           right = mid -1
        elif arr[mid] < key:
            left = mid + 1
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
                lowerBound = lower_bound(arr_sort, key, n)
                print(lowerBound)
            else:
                print('mang rong')
            break
        except ValueError:
            print('Dinh dang dau vao khong hop le!')