# Bài 17. Mảng gần như đã sắp xếp
# Khi mảng gần sắp xếp (ít nghịch thế), chứng minh insertion sort chạy gần O(n). Đo số shift
# trên mảng chỉ có vài cặp sai vị trí.
# Ví dụ: a = [1, 2, 4, 3, 5] → chỉ 1 shift

def almost_insertionSort(arr,n):
    shift = 0
    arr_ = arr.copy()
    for i in range(1,n):
        x = arr_[i]
        j = i-1
        while j >=0 and arr_[j] > x:
            arr_[j+1] = arr_[j]
            shift +=1
            j -=1
        arr_[j+1] = x
    return arr, shift

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if len(arr) > 0:
                sorted_arr, shift = almost_insertionSort(arr,n)
                print(f'{sorted_arr} -> {shift} shift')
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')



                