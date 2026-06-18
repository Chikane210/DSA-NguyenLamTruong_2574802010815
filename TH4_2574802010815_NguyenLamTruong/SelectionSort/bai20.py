# Bài 20. Liên hệ với heap sort
# Heap sort có thể coi là selection sort cải tiến: thay vì quét O(n) tìm max, dùng heap lấy max
# trong O(log n). Trình bày mối liên hệ và độ phức tạp O(n log n).
# Ví dụ: selection O(n²) → heap sort O(n log n)

def heapify(arr, n, i):
    root = i          
    left = 2 * i + 1    
    right = 2 * i + 2    
    if left < n and arr[left] > arr[root]:
        root = left
    if right < n and arr[right] > arr[root]:
        root = right
    if root != i:
        arr[i], arr[root] = arr[root], arr[i]  
        heapify(arr, n, root)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                heap_sort(arr)
                print(arr)
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')