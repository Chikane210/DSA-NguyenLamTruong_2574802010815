# Bài 20. Shell sort
# Cài đặt Shell sort — tổng quát hóa insertion sort với khoảng cách (gap) giảm dần. Thử dãy
# gap khác nhau (n/2, dãy Knuth) và so sánh số shift.
# Ví dụ: gap = 4, 2, 1 trên mảng cỡ 8

def shellSort(arr,n):
    gap = n // 2
    shift = 0
    arr_ = arr.copy()
    while gap > 0:
        for i in range (gap,n):
            key = arr_[i]
            j = i
            while j>= gap and arr_[j-gap] > key:
                arr_[j] = arr_[j-gap]
                shift +=1
                j -=gap
            arr_[j] = key
        gap //= 2
    return arr_, shift

def shellSort_knuth(arr,n): #h = 3h +1
    shift = 0
    arr_ = arr.copy()
    h = 1
    while h < n//3:
        h = h*3 +1
    while h > 0:
        for i in range (h,n):
            key = arr_[i]
            j = i
            while j >=h and arr_[j-h] > key:
                arr_[j] = arr_[j-h]
                shift +=1
                j -=h
            arr_[j] = key
        h //= 3
    return arr_, shift

def insertionSort(arr, n):
    shift =0
    arr_ = arr.copy()
    for i in range(1,n):
        key = arr_[i]
        j = i-1
        while j>=0 and arr_[j] > key:
            arr_[j+1] = arr_[j]
            shift+=1
            j -=1
        arr_[j+1] = key
    return arr_, shift

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                sorted_1, shift_1 = shellSort(arr,n)
                sorted_2, shift_2 = insertionSort(arr,n)
                sorted_3, shift_3 = shellSort_knuth(arr,n)
                print(f'Shell Sort: {sorted_1} -> {shift_1} shift')
                print(f'Insertion Sort: {sorted_2} -> {shift_2} shift')
                print(f'Shell Sorted (Knuth): {sorted_3} -> {shift_3} shift')
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')