# Bài 9. Double selection sort
# Cải tiến: mỗi vòng tìm cả phần tử nhỏ nhất và lớn nhất, đặt nhỏ nhất về đầu và lớn nhất
# về cuối. Giảm số vòng còn một nửa. So sánh số so sánh với bản thường.
# Ví dụ: a = [5, 1, 4, 2, 8] → [1, 2, 4, 5, 8]

def doubleSelectionSort(arr,n):
    compare = 0
    arr_ = arr.copy()
    for i in range(n//2):
        min_pos = i
        max_pos = i
        for j in range(i+1,n-i):
            compare +=1
            if arr_[j] < arr_[min_pos]:
               min_pos = j
            compare +=1
            if arr_[j] > arr_[max_pos]:
                max_pos = j
        arr_[i], arr_[min_pos] = arr_[min_pos], arr_[i]
        if max_pos == i:
            max_pos = min_pos
        arr_[n-i-1], arr_[max_pos] = arr_[max_pos], arr_[n-i-1]     
    return arr_, compare

def selectionSort(arr,n):
    compare = 0
    arr_ = arr.copy()
    for i in range(n-1):
        min_pos = i
        for j in range(i+1,n):
            compare +=1
            if arr_[j] < arr_[min_pos]:
                min_pos = j
        arr_[i], arr_[min_pos] = arr_[min_pos], arr_[i]
    return arr_, compare

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                sorted_1, compare_1 = doubleSelectionSort(arr,n)
                sorted_2, compare_2 = selectionSort(arr,n)
                print(f'Double Selection Sort: {sorted_1} -> {compare_1} compare')
                print(f'Selection Sort: {sorted_2} -> {compare_2} compare')
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')