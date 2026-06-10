# Bài 10. Đếm số lượt cần thiết
# Đếm số lượt bubble sort (bản tối ưu early-exit) cần để mảng được sắp xếp xong.
# Ví dụ: a = [2, 1, 3, 4] → 2 lượt

def count_bubbleSort_earlyExit(arr,n):
    turn = 0
    for i in range (n-1):
        swapped = False
        turn += 1
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            return turn

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                print(count_bubbleSort_earlyExit(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap vao so nguyen')