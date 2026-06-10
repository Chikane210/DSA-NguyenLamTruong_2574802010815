# Bài 22. Mảng gần sắp xếp với độ lệch ≤ k
# Mỗi phần tử cách vị trí đúng của nó tối đa k vị trí. Chứng minh bubble sort (early-exit) chạy
# trong O(n·k) và kiểm nghiệm bằng đo số lượt.
# Ví dụ: n = 10^4, k = 3 → rất nhanh so với O(n²)

def xao_tron_mang(n,k):
    arr = list(range(0,n))
    for i in range(0,n,k+1):
        mang_con = arr[i:i+k+1]
        mang_con = mang_con[::-1]
        arr[i:i+k+1] = mang_con
    return arr

def bubbleSort_Earlyexit(arr):
    n = len(arr)
    turn = 0
    swap = 0
    for i in range(n-1):
        swapped = False
        turn +=1
        for j in range (n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap += 1
                swapped = True
        if swapped == False:
            return turn, swap
    return turn, swap

if __name__ == '__main__':
    while True:
        try:
            n = int(input('n: '))
            k = int(input('k: '))
            if k > 0 and n > 0:
                mang_da_xao_tron = xao_tron_mang(n,k)
                turn, swap = bubbleSort_Earlyexit(mang_da_xao_tron)       
                print(f'So luot: {turn}\nHoan doi: {swap}')
                break
            print('n va k phai lon hon 0')
        except ValueError:
            print('nhap so nguyen')