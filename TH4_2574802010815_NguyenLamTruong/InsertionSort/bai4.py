# Bài 4. In mảng sau mỗi bước chèn
# Sau mỗi vòng lặp ngoài (chèn xong phần tử thứ i), in trạng thái mảng. Phần đầu mảng luôn
# được sắp xếp dần.
# Ví dụ: a = [3, 1, 2] → [1,3,2] rồi [1,2,3]

def insertionSort(arr,n):
    matrix = []
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
        arr_ = arr.copy()
        matrix.append(arr_)
    return matrix

def in_buoc_chen(arr):
    for i in arr:
        print(i, end=' ')

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if len(arr) > 0:
                insertion_sort = insertionSort(arr,n)
                in_buoc_chen(insertion_sort)
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')
