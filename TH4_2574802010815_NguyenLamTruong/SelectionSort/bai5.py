# ài 5. Đếm số lần hoán đổi
# Sắp xếp tăng dần và đếm số lần hoán đổi. Selection sort dùng tối đa n-1 swap.
# Ví dụ: a = [3, 2, 1] → ≤ 2 swap

def selectionSort(arr,n):
    swap = 0
    for i in range(n-1):
        min_pos = i
        for j in range(i+1,n):
            if arr[j] < arr[min_pos]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
        swap +=1
    return swap

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                print(f'{arr}->{selectionSort(arr,n)}')
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')