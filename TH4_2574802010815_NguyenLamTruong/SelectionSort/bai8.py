# Bài 8. Tìm chỉ số nhỏ nhất trong đoạn [i, n)
# Viết hàm trả về chỉ số phần tử nhỏ nhất trong đoạn từ vị trí i tới cuối — bước lõi của
# selection sort.
# Ví dụ: a = [9, 3, 7, 1, 5], i = 1 → chỉ số 3

def find_min_pos(arr,i,n):
    for pos in range (i, n):
        min_pos = i
        if arr[pos] < arr[min_pos]:
            min_pos = pos
    return min_pos

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            i = int(input('i: '))
            n = len(arr)
            if n > 0:
                print(f'Chi so {find_min_pos(arr,i,n)}')
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')        