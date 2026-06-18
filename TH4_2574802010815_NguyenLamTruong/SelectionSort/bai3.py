# Bài 3. Sắp xếp giảm dần
# Cài đặt selection sort theo thứ tự giảm dần (mỗi vòng chọn phần tử lớn nhất).
# Ví dụ: a = [5, 2, 4, 6, 1] → [6, 5, 4, 2, 1]

def selectionSort(arr,n):
    for i in range(n-1):
        max_pos = i
        for j in range(i+1,n):
            if arr[j] > arr[max_pos]:
                max_pos = j
        arr[i], arr[max_pos] = arr[max_pos], arr[i]
    return arr

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                print(selectionSort(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')