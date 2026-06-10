# Bài 11. Sắp xếp theo trị tuyệt đối
# Sắp xếp mảng tăng dần theo |a[i]|. Nếu trị tuyệt đối bằng nhau, giữ nguyên thứ tự xuất hiện.
# Ví dụ: a = [-3, 1, -2, 2] → [1, -2, 2, -3]

def bubbleSort_abs(arr, n):
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if abs(arr[j]) > abs(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            return arr
        
if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                print(bubbleSort_abs(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap vao so nguyen')