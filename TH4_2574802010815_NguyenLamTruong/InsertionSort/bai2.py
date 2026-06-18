# Bài 2. Sắp xếp tăng dần cơ bản
# Cài đặt insertion sort sắp xếp mảng số nguyên theo thứ tự tăng dần.
# Ví dụ: a = [5, 2, 4, 6, 1, 3] → [1, 2, 3, 4, 5, 6]
# Ràng buộc: 1 ≤ n ≤ 10^3

def insertionSort(arr, n):
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if len(arr) > 0:
                print(insertionSort(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')
