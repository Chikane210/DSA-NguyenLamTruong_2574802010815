# Bài 22. Mảng độ lệch ≤ k
# Mỗi phần tử cách vị trí đúng tối đa k. Chứng minh insertion sort chạy trong O(n·k) và kiểm
# nghiệm bằng số shift.
# Ví dụ: n = 10^4, k = 3 → nhanh hơn nhiều O(n²)

from random import randint
def xao_tron_mang(n,k):
    arr = list(range(0,n))
    for i in range(0,n,k+1):
        mangcon = arr[i:i+k+1]
        mangcon = mangcon[::-1]
        arr[i:i+k+1] = mangcon
    return arr

def insertionSort_with_dolechK(arr,n):
    shift = 0
    for i in range (1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
            shift +=1
        arr[j+1] = key
    return shift

def insertionSort(arr,n):
    shift = 0
    for i in range (1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
            shift +=1
        arr[j+1] = key
    return shift

if __name__ == '__main__':
    while True:
        try:
            n = int(input('n: '))
            k = int(input('k: '))
            mang_xao_tron = xao_tron_mang(n,k)
            mang_ngau_nhien = [randint(0,n) for x in range(0,n)]
            if n > 0:
                shift_1 = insertionSort_with_dolechK(mang_xao_tron,n)
                shift_2 = insertionSort(mang_ngau_nhien,n)
                print(f'Mang do lech K: {shift_1} shift')
                print(f'Mang binh thuong: {shift_2} shift')
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')