# Bài 3. Sắp xếp giảm dần
# Cài đặt insertion sort sắp xếp mảng theo thứ tự giảm dần.
# Ví dụ: a = [5, 2, 4, 6, 1] → [6, 5, 4, 2, 1]

def insertionSort_down(arr,n):
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] < key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if len(arr) > 0:
                print(insertionSort_down(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')
        