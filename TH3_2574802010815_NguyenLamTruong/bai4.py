# Bài 4. Đếm số lần hoán đổi
# Sắp xếp tăng dần và đếm tổng số lần hoán đổi (swap) đã thực hiện.
# Ví dụ: a = [3, 2, 1] → 3 lần 

def bubbleSort_plus(arr, n):
    swap = 0
    for i in range (n-1):
        swapped = False
        for j in range (n-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swap +=1
                swapped = True
        if swapped == False:
            break
    return swap 

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                print(bubbleSort_plus(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap vao so nguyen')