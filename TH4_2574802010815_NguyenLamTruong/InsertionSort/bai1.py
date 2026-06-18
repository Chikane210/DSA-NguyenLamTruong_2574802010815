# Bài 1. Chèn một phần tử vào mảng đã sắp xếp
# Cho mảng a đã sắp xếp tăng dần và số x. Chèn x vào đúng vị trí để mảng vẫn tăng dần.
# Ví dụ: a = [1, 3, 5, 7], x = 4 → [1, 3, 4, 5, 7]

def insert_x(arr, x):
    arr.append(x)
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            x = int(input('x: '))
            if len(arr) > 0:
                print(insert_x(arr,x))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')
