# Bài 2. Sắp xếp tăng dần cơ bản
# Cài đặt selection sort sắp xếp mảng số nguyên theo thứ tự tăng dần.
# Ví dụ: a = [5, 2, 4, 6, 1, 3] → [1, 2, 3, 4, 5, 6]

def selectionSort(arr,n):
    for i in range(n-1):
        min_pos = i
        for j in range(i+1,n):
            if arr[j] < arr[min_pos]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return arr

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                print(selectionSort(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')