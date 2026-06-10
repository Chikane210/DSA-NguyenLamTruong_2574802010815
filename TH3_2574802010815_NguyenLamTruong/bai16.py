# Bài 16. Số nghịch thế = số swap
# Chứng minh và tính: số lần hoán đổi của bubble sort đúng bằng số nghịch thế (số cặp i < j
# mà a[i] > a[j]).
# Ví dụ: a = [2, 3, 1] → 2 nghịch thế = 2 swap

def count_swap(arr, n):
    swap = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap +=1
    return swap

def count_nghich_the(arr, n):
    nghich_the = 0
    for i in range (n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                nghich_the +=1
    return nghich_the

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            arr_swap = arr.copy()
            arr_nghichthe = arr.copy()
            if n > 0:
                print('Swap',count_swap(arr_swap,n))
                print('Nghich the', count_nghich_the(arr_nghichthe,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen') 
    


