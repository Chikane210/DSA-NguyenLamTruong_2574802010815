# Bài 6. Phần tử nào về đúng chỗ sau 1 lượt
# Sau một lượt bubble sort tăng dần, phần tử lớn nhất luôn nằm ở cuối. Cho mảng, in ra giá
# trị nằm ở vị trí cuối a[n-1] sau 1 lượt.
# Ví dụ: a = [4, 2, 7, 1, 3] → 7

def correct_pos(arr, n):
    for i in range(n-1):
        for j in range (n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        break
    return arr[-1]

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                print(correct_pos(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap vao so nguyen')
        