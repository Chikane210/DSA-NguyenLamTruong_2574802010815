# Bài 5. Đếm số lần dịch chuyển
# Sắp xếp tăng dần và đếm tổng số lần dịch chuyển phần tử (shift).
# Ví dụ: a = [3, 2, 1] → 3 lần dịch

def count_swap(arr, n):
    count = 0
    for i in range (1,n):
        key = arr[i]
        j = i-1
        while j >=0 and arr[j] > key:
            count += 1
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return count

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if len(arr) > 0:
                print(count_swap(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')