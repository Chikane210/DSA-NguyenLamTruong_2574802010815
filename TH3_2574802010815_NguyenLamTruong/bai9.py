# Bài 9. Bubble sort tối ưu (early exit)
# Cải tiến bubble sort: nếu trong một lượt không có lần hoán đổi nào thì dừng ngay. Cho biết
# với mảng đã sắp xếp sẵn, thuật toán chạy bao nhiêu lượt.
# Ví dụ: a = [1, 2, 3, 4] → 1 lượt rồi dừng

def bubbleSort_earlyExit(arr,n):
    turn = 0
    for i in range(n-1):
        turn +=1
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            return arr, turn
    return arr, turn

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                arr_bubbleSort, turn = bubbleSort_earlyExit(arr,n)
                print(f'{arr_bubbleSort} -> {turn} luot')
                break
            print('mang rong')
        except ValueError:
            print('nhap vao so nguyen')