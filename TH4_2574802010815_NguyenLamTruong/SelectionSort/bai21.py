# Bài 21. Chứng minh số so sánh cố định
# Chứng minh selection sort luôn thực hiện đúng n(n-1)/2 phép so sánh, không phụ thuộc đầu
# vào (không có best case nhanh hơn).

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
                compare = count_compare(arr,n)
                lythuyet = n*(n-1) / 2
                if compare == lythuyet:
                    print(f'Selection Sort thuc hien dung n(n-1)/2 phép so sánh - {compare} compare')
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')
        