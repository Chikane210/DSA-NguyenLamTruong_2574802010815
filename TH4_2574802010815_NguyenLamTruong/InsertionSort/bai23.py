# Bài 23. Phân tích best / average / worst
# Phân tích số so sánh và số shift của insertion sort trên 3 đầu vào: đã sắp xếp, ngẫu nhiên, sắp
# xếp ngược. Lập bảng đối chiếu với lý thuyết.
# Ví dụ: best = O(n), average = worst = O(n²)
import time
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

if __name__ == '__main__':
    while True:
        try:
            n = int(input('n: '))
            if n > 0:
                randomElement_arr = [randint(0,n) for x in range(0,n)]
                sorted_arr = list(range(0,n))
                reverse_arr = list(range(0,n))[::-1]

                print('Mang ngau nhien')
                start_time = time.time()
                compare, shift = insertionSort(randomElement_arr,n)
                end_time = time.time()
                print(f'Comapare: {compare} - Shift: {shift}\nThoi gian thuc hien: {end_time - start_time:.10f}')
                print('-'*30)
                
                print('Mang da sap xep')
                start_time = time.time()
                compare, shift = insertionSort(sorted_arr,n)
                end_time = time.time()
                print(f'Comapare: {compare} - Shift: {shift}\nThoi gian thuc hien: {end_time - start_time:.10f}')
                print('-'*30)
                
                print('Mang nguoc')
                start_time = time.time()
                compare, shift = insertionSort(reverse_arr,n)
                end_time = time.time()
                print(f'Comapre: {compare} - Shift: {shift}\nThoi gian thuc hien: {end_time - start_time:.10f}')    
                break
            print('mang rong')
        except ValueError:
            print('nhap vao so nguyen')