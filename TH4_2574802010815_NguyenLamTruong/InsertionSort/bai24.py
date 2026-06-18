# Bài 24. So sánh 3 thuật toán O(n²)
# Đo và so sánh số swap/shift và số so sánh của insertion, bubble và selection sort trên cùng
# tập dữ liệu. Rút ra khi nào nên dùng insertion sort.
# Ví dụ: trình bày bảng số liệu 3 thuật toán
from random import randint

def insertionSort(arr, n):
    compare, shift = 0, 0
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0:
            compare+=1
            if arr[j] > key:
                arr[j+1] = arr[j]
                shift+=1
                j -=1
            else:
                break
        arr[j+1] = key
    return compare, shift

def bubbleSort(arr,n):
    compare, swap = 0, 0
    arr_ = arr.copy()
    for i in range(n-1):
        for j in range(n-i-1):
            compare +=1
            if arr_[j] > arr_[j+1]:
                arr_[j], arr_[j+1] = arr_[j+1], arr_[j]
                swap +=1
    return compare, swap

def selectionSort(arr,n):
    compare, swap = 0, 0
    arr_ = arr.copy()
    for i in range(n-1):
        min_pos = i
        for j in range(i+1,n):
            compare +=1
            if arr_[j] < arr_[min_pos]:
                min_pos = j
        if arr[i] != arr[min_pos]:
            arr_[i], arr_[min_pos] = arr_[min_pos], arr_[i]
            swap +=1
    return compare, swap

if __name__ == '__main__':
    while True:
        try:
            n = int(input('n: '))
            mang_ngau_nhien = [randint(0,n) for x in range(0,n)]
            mang_nguoc = list(range(0,n))[::-1]
            mang_sap_xep = list(range(0,n))
            
            is_compare_1, is_shift_1 = insertionSort(mang_ngau_nhien, n)
            is_compare_2, is_shift_2 = insertionSort(mang_nguoc, n)
            is_compare_3, is_shift_3 = insertionSort(mang_sap_xep, n)
            
            bs_compare_1, bs_swap_1 = bubbleSort(mang_ngau_nhien,n)
            bs_compare_2, bs_swap_2 = bubbleSort(mang_nguoc,n)
            bs_compare_3, bs_swap_3 = bubbleSort(mang_sap_xep,n)
            
            ss_compare_1, ss_swap_1 = selectionSort(mang_ngau_nhien,n)
            ss_compare_2, ss_swap_2 = selectionSort(mang_nguoc,n)
            ss_compare_3, ss_swap_3 = selectionSort(mang_sap_xep,n)
            if n > 0:
                print('Bubble Sort:')
                print(f'Mang ngau nhien: compare -> {bs_compare_1} | swap -> {bs_swap_1}')
                print(f'Mang nguoc: compare -> {bs_compare_2} | swap -> {bs_swap_2}')
                print(f'Mang sap xep: compare -> {bs_compare_3} | swap -> {bs_swap_3}')
                print('-'*30)
                
                print('Insertion Sort:')
                print(f'Mang ngau nhien: compare -> {is_compare_1} | swap -> {is_shift_1}')
                print(f'Mang nguoc: compare -> {is_compare_2} | swap -> {is_shift_2}')
                print(f'Mang sap xep: compare -> {is_compare_3} | swap -> {is_shift_3}')
                print('-'*30)
                
                print('Selection Sort:')
                print(f'Mang ngau nhien: compare -> {ss_compare_1} | swap -> {ss_swap_1}')
                print(f'Mang nguoc: compare -> {ss_compare_2} | swap -> {ss_swap_2}')
                print(f'Mang sap xep: compare -> {ss_compare_3} | swap -> {ss_swap_3}')
                print('-'*30)
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')
#Nên dùng insertion sort trên mảng gần/đã sắp xếp