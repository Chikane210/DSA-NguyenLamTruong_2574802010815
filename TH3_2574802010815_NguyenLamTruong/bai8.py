# Bài 8. Kiểm tra đã sắp xếp sau k lượt
# Cho mảng và số k. Thực hiện k lượt bubble sort rồi cho biết mảng đã được sắp xếp hoàn toàn
# chưa (true/false).
# Ví dụ: a = [3, 2, 1], k = 1 → false

def k_bubbleSort(arr,k,n):
    for i in range(k):
        flag = True
        for j in range (n-i-1):
            if arr[j] > arr[j+1]:
                flag = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
    if flag == True:
        return flag
    return flag

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            k = int(input())
            n = len(arr)
            if n > 0:
                print(k_bubbleSort(arr,k,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap vao so nguyen')