# Bài 16. Sắp xếp theo trị tuyệt đối
# Sắp xếp tăng dần theo |a[i]| bằng selection sort.
# Ví dụ: a = [-3, 1, -2, 2] → [1, -2/2..., -3]

def abs_selectionSort(arr,n):
    for i in range(n-1):
        min_pos = i
        for j in range(i+1,n):
            if abs(arr[j]) < abs(arr[min_pos]):
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return arr

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                print(abs_selectionSort(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')