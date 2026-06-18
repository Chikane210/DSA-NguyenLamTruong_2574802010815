# Bài 10. Số shift = số nghịch thế
# Chứng minh và tính: tổng số lần dịch chuyển của insertion sort đúng bằng số nghịch thế
# của mảng.
# Ví dụ: a = [2, 4, 1, 3] → 3 nghịch thế = 3 shift

def sum_swap(arr,n):
    swap = 0
    for i in range (1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            swap +=1
            j -=1
        arr[j+1] = key
    return swap

def so_nghichthe(arr,n):
    nghich_the = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] > arr[i]:
                nghich_the += 1
    return nghich_the

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            arr_1 = arr.copy()
            arr_2 = arr.copy()
            if n > 0:
                sumSwap = sum_swap(arr_1, n)
                so_nghich_the = so_nghichthe(arr_2,n)
                print('So lan dich chuyen:', sumSwap)
                print('So nghich the:', so_nghich_the)
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')