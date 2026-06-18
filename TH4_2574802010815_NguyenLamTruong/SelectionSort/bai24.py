# Bài 24. Tìm k nhỏ nhất: partial selection vs heap
# So sánh hai cách lấy k phần tử nhỏ nhất: partial selection O(n·k) và dùng heap O(n + k log n).
# Cho biết khi nào mỗi cách tốt hơn.
# Ví dụ: k nhỏ → selection; k lớn → heap
from random import randint
import time
def partial_selection(arr, k, n):
    for i in range(k):
        min_pos = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_pos]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return arr[:k]

def heapify(arr, n, i):
    root = i          
    left = 2 * i + 1     
    right = 2 * i + 2    
    
    if left < n and arr[left] < arr[root]:
        root = left
    if right < n and arr[right] < arr[root]:
        root = right
        
    if root != i:
        arr[i], arr[root] = arr[root], arr[i]  
        heapify(arr, n, root) 

def min_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
def find_min_k_heap(arr, k):
    n = len(arr)
    if k <= 0: return []
    if k > n: k = n  
    min_heap(arr)
    result = []
    heap_size = n
    for i in range(k):
        result.append(arr[0]) 
        arr[0] = arr[heap_size - 1]
        heap_size -= 1
        heapify(arr, heap_size, 0)  
    return result

if __name__ == "__main__":
    while True:
        try:
            n = int(input('n: '))
            k = int(input('k: '))
            random_element = [randint(0,n) for x in range(0,n)]
            arr_1 = random_element.copy()
            arr_2 = random_element.copy()
            if n > 0:
                print('---Partial Selection---')
                start_time = time.time()
                partialSelection = partial_selection(arr_1,k,n)
                end_time = time.time()
                print(f'Thoi gian thuc hien:{end_time-start_time:.10f} ')
                
                print('---Min Heap---')
                start_time = time.time()
                minHeap = find_min_k_heap(arr_2,k)
                end_time = time.time()
                print(f'Thoi gian thuc hien:{end_time-start_time:.10f} ')
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')