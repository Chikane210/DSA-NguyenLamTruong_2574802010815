# Bài 13. Phần tử đơn lẻ trong mảng đôi
# Mọi phần tử xuất hiện đúng 2 lần trừ một phần tử duy nhất. Mảng đã sắp xếp. Tìm phần tử
# đơn lẻ trong O(log n).
# Ví dụ: a = [1, 1, 2, 3, 3, 4, 4] → 2

def ptu_don_le(arr, n):
    left = 0
    right = n -1
    single = 0
    while left <= right:
        mid = (left + right) // 2
        if mid % 2 != 0:
            mid = mid -1
        if arr[mid] == arr[mid+1]:
            left = mid +2
        else:
            single = arr[mid]
            right = mid -1
    return single

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                arr_sort = sorted(arr)
                print(ptu_don_le(arr_sort,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')