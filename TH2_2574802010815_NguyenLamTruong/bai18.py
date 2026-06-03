# Bài 18. Phần tử thứ K bị thiếu (Kth Missing Positive)
# Mảng số dương tăng dần. Tìm số nguyên dương thứ k bị thiếu.
# Ví dụ: a = [2,3,4,7,11], k = 5 → 9

def find_KthPos(arr, k,n):
    left = 0 
    right = n -1
    while left <= right:
        mid = (left + right) // 2
        so_bi_thieu = arr[mid] - (mid+1)
        if so_bi_thieu < k:
            left = mid +1
        else:
            right = mid -1
    return left + k

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            k = int(input('k: '))
            if n > 0:
                print(find_KthPos(arr, k,n))
                break
            else:
                print('mang rong')
        except ValueError:
            print('nhap so nguyen')