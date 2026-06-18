# Bài 11. Sắp xếp theo trị tuyệt đối (ổn định)
# Sắp xếp tăng dần theo |a[i]|; nếu bằng nhau giữ nguyên thứ tự xuất hiện (tận dụng tính ổn
# định của insertion sort).
# Ví dụ: a = [-3, 1, -2, 2] → [1, -2, 2, -3]

def abs_insertionSort(arr, n):
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and abs(arr[j]) > abs(key):
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if len(arr) > 0:
                print(abs_insertionSort(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')