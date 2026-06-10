# Bài 17. Sắp xếp một phần (k phần tử lớn nhất)
# Chỉ cần k phần tử lớn nhất nằm đúng ở cuối mảng. Thực hiện đúng k lượt bubble sort và trả
# về mảng.
# Ví dụ: a = [3, 1, 4, 1, 5], k = 2 → [...,4,5]

def sortApart(arr,n,k):
    for i in range (k):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr[n-k:n]

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            k = int(input('k: '))
            if n > 0:
                print(sortApart(arr,n,k))
                break
            print('mang rong')
        except ValueError:
            print('nhap vao so nguyen')