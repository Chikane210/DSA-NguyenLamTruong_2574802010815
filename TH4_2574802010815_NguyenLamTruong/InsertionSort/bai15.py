# Bài 9. Binary insertion sort
# Cải tiến: dùng tìm kiếm nhị phân để xác định vị trí chèn (giảm số so sánh xuống O(log i)),
# sau đó vẫn dịch chuyển để chèn. Đếm số so sánh và so với bản thường.
# Ví dụ: giảm số so sánh nhưng số shift không đổi
from random import randint
def insertionSort(arr, n): 
    compare = 0
    shift = 0
    arr_ = arr.copy()  
    for i in range(1, n):
        key = arr_[i]
        j = i - 1
        while j >= 0:
            compare += 1
            if arr_[j] > key:
                arr_[j + 1] = arr_[j]
                shift += 1
                j -= 1
            else:
                break
        arr_[j + 1] = key    
    return compare, shift


def binary_search_position(arr, key, left, right, counter_dict):
    while left <= right:
        mid = (left + right) // 2
        counter_dict['comps'] += 1      
        if arr[mid] == key:
            return mid + 1
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1      
    return left


def binary_insertion_sort(arr, n):
    counter = {'comps': 0}
    shift = 0
    arr_ = arr.copy()
    for i in range(1, n):
        key = arr_[i]
        pos = binary_search_position(arr_, key, 0, i - 1, counter)
        for j in range(i - 1, pos - 1, -1):
            arr_[j + 1] = arr_[j]
            shift += 1
        arr_[pos] = key
    return counter['comps'], shift

if __name__ == '__main__':
    while True:
        try:
            n = int(input('n: '))
            arr = [randint(0,n) for x in range(0,n)]
            if n > 0:
                compare1, shift1 = insertionSort(arr, n)
                compare2, shift2 = binary_insertion_sort(arr, n)
                print(f'Insert Sort')
                print(f'Compare: {compare1} | Shift: {shift1}')
                
                print(f'Binary Insertion Sort:')
                print(f'Compare: {compare2} | Shift: {shift2}')
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')