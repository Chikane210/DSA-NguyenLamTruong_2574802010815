# Bài 23. Phân tích & so sánh hiệu năng
# Đo số so sánh và số swap của bubble sort trên 3 loại đầu vào: ngẫu nhiên, đã sắp xếp, sắp
# xếp ngược. Vẽ/trình bày bảng so sánh với độ phức tạp lý thuyết O(n²).
# Ví dụ: best = O(n), average = worst = O(n²)

import time
import random

def bubbleSort(arr):
    n = len(arr)
    compare = 0
    swap = 0
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            compare += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                swap +=1
        if swapped == False:
            return compare, swap
    return compare, swap

if __name__ == '__main__':
    while True:
        try:
            n = int(input('n: '))
            if n > 0:
                randomElement_arr = [random.randint(0,n) for x in range(0,n)]
                sorted_arr = list(range(0,n))
                reverse_arr = list(range(0,n))[::-1]

                print('Mang ngau nhien')
                start_time = time.time()
                turn, swap = bubbleSort(randomElement_arr)
                end_time = time.time()
                print(f'Turn: {turn} - Swap: {swap}\nThoi gian thuc hien: {end_time - start_time:.10f}')
                print('-'*30)
                
                print('Mang da sap xep')
                start_time = time.time()
                turn, swap = bubbleSort(sorted_arr)
                end_time = time.time()
                print(f'Turn: {turn} - Swap: {swap}\nThoi gian thuc hien: {end_time - start_time:.10f}')
                print('-'*30)
                
                print('Mang nguoc')
                start_time = time.time()
                turn, swap = bubbleSort(reverse_arr)
                end_time = time.time()
                print(f'Turn: {turn} - Swap: {swap}\nThoi gian thuc hien: {end_time - start_time:.10f}')    
                break
            print('mang rong')
        except ValueError:
            print('nhap vao so nguyen')