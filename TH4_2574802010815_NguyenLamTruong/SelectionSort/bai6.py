# Bài 6. Đếm số lần so sánh
# Sắp xếp tăng dần và đếm số lần so sánh. Selection sort luôn dùng n(n-1)/2 so sánh bất kể
# đầu vào — hãy kiểm chứng.
# Ví dụ: n = 5 → luôn 10 lần so sánh


def count_compare(arr,n):
    compare = 0
    for i in range(n-1):
        min_pos = i
        for j in range(i+1,n):
            compare +=1
            if arr[j] < arr[min_pos]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return compare

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                print(f'n = {n} -> {count_compare(arr,n)}')
                print(f'Ly thuyet: {n*(n-1)/2}')
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')