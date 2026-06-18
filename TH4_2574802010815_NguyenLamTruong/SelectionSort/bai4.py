# Bài 4. In mảng sau mỗi vòng chọn
# Sau mỗi vòng (đặt xong phần tử nhỏ thứ i), in trạng thái mảng. Phần đầu mảng đã được sắp
# xếp cố định.
# Ví dụ: a = [3, 1, 2] → [1,3,2] rồi [1,2,3]

def selectionSort(arr,n):
    matrix = []
    for i in range(n-1):
        min_pos = i
        for j in range(i+1,n):
            if arr[j] < arr[min_pos]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
        matrix.append(arr.copy())
    return matrix

def in_buoc_hoandoi(arr):
    for i in arr:
        print(i, end=' ')
        
if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if len(arr) > 0:
                insertion_sort = selectionSort(arr,n)
                in_buoc_hoandoi(insertion_sort)
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')
