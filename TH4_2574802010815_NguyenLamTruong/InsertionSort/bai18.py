# Bài 18. Chèn từ cuối hay đầu?
# So sánh hai cách dò vị trí chèn: dò từ phải sang trái (chuẩn) vs dò từ trái sang phải. Giải thích
# vì sao dò từ phải hiệu quả hơn với dữ liệu gần sắp xếp.
# Ví dụ: phân tích số phép so sánh hai chiến lược

def rightToleft_insertionSort(arr,n):
    shift = 0
    compare = 0
    for i in range(1,n):
        pos = 0
        x = arr[i]
        while pos < i:
            compare +=1
            if arr[pos] > x:
                break
            pos +=1
        for j in range(i,pos,-1):
            arr[j] = arr[j-1]
            shift +=1
        arr[pos] = x    
    return arr, shift, compare

def insertionSort(arr, n):
    shift = 0
    compare = 0
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            compare +=1
            arr[j+1] = arr[j]
            shift +=1
            j -=1
        arr[j+1] = key
    return arr, shift, compare

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                arr_1 = arr.copy()
                arr_2 = arr.copy()
                print('---Dò từ phải sang trái---')
                sorted_arr_1, shift_1, compare_1 = insertionSort(arr_1,n)
                print(f'{sorted_arr_1} -> {shift_1} shift, {compare_1} compare')
                print('---Dò từ trái sang phải---')
                sorted_arr_2, shift_2, compare_2 = rightToleft_insertionSort(arr_2,n)
                print(f'{sorted_arr_2} -> {shift_2} shift, {compare_2} compare')
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')
# Đối với mảng gần sắp xếp thì insertion sort từ phải sang trái sẽ tối ưu hơn vì nó sẽ dừng lại ngay khi phần tử đã 
# đúng vị trí còn insertion sort phải duyệt thêm các phần tử cho đến vị trí pos dù phần tử đó đã nằm đúng vị trí
