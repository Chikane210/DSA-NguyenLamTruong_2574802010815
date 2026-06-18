# Bài 6. Đếm số lần so sánh
# Sắp xếp tăng dần và đếm tổng số lần so sánh giữa các phần tử.
# Ví dụ: a = [1, 2, 3] (best case) → 2 lần so sánh

def count_compare(arr,n):
    compare = 0
    for i in range(1,n):
        swap = False
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            swap = True
            j -=1
        arr[j+1] = key
        if swap == True:
            compare +=1
    return compare

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if len(arr) > 0:
                print(count_compare(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')