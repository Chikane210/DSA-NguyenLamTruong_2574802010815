# Bài 16. Sắp xếp trực tuyến (online)
# Các phần tử đến lần lượt theo luồng. Sau mỗi phần tử mới, giữ cho mảng luôn được sắp
# xếp. Đây chính là bản chất "online" của insertion sort.
# Ví dụ: thêm 5,2,8,1 → [5],[2,5],[2,5,8],[1,2,5,8]

def insertion_onineSort(arr,n):
    matrix = [[arr[0]]]
    for i in range(1,n):
        x = arr[i]
        j = i-1
        while j>=0 and arr[j] > x:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = x
        arr_ = arr.copy()
        matrix.append(arr_[0:i+1])
    return matrix
def in_buoc_chen(arr):
    for i in arr:
        print(i, end=' ')

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if len(arr) > 0:
                insertion_sort = insertion_onineSort(arr,n)
                in_buoc_chen(insertion_sort)
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')       