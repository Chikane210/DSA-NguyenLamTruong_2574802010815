# Bài 21. Đếm shift cho mảng lớn
# Tính tổng số shift của insertion sort cho mảng cỡ lớn không mô phỏng O(n²), mà bằng đếm
# nghịch thế trong O(n log n) (merge sort hoặc BIT).
# Ví dụ: n ≤ 10^5

def mergeSort(arr):
    result = []
    if len(arr) < 2:
        return arr
    mid = int(len(arr)/2)
    y = mergeSort(arr[:mid])
    z = mergeSort(arr[mid:])
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                y.pop(0)
    return result

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if len(arr) > 0:
                print(mergeSort(arr))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')