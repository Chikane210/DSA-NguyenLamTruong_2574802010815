# Bài 3. Sắp xếp giảm dần
# Cài đặt bubble sort sắp xếp mảng theo thứ tự giảm dần.
# Ví dụ: a = [5, 1, 4, 2, 8] → [8, 5, 4, 2, 1]

def bubbleSort(arr,n):
    for i in range (n-1):
        for j in range (n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                print(bubbleSort(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap vao so nguyen')