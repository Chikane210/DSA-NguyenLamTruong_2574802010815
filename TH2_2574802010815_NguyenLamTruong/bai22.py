# Bài 22. Median của hai mảng đã sắp xếp
# Cho hai mảng đã sắp xếp a (cỡ m) và b (cỡ n). Tìm trung vị của hợp hai mảng trong
# O(log(min(m,n))).
# Ví dụ: a = [1,3], b = [2] → 2.0 ; a = [1,2], b = [3,4] → 2.5

def median(arr, n):
    left = 0 
    right = n -1
    mid = (left + right) // 2
    if n % 2 == 0:
        median = (arr[mid] + arr[mid+1]) / 2
    else:
        median = arr[mid]
    return median

if __name__ == '__main__':
    while True:
        try:
            arr_a = [int(x) for x in input().split()]
            arr_b = [int(x) for x in input().split()]
            arr_ab = sorted(arr_a + arr_b)
            n = len(arr_ab)
            if n > 0:
                print(median(arr_ab, n))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')