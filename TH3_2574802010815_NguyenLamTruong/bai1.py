# Bài 1. Thực hiện một lượt (one pass)
# Cho mảng a. Thực hiện đúng một lượt của bubble sort (duyệt từ trái sang phải, hoán đổi cặp
# liền kề nếu sai thứ tự tăng dần) và in ra mảng sau lượt đó.
# Ví dụ: a = [5, 1, 4, 2, 8] → [1, 4, 2, 5, 8]

def bubbleSort_onepass(arr, n):
    for j in range (n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                print(bubbleSort_onepass(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap vao so nguyen')
    