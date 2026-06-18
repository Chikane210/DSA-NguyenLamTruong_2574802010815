# Bài 18. So sánh số swap với bubble sort
# Trên cùng tập dữ liệu, so sánh số swap của selection sort (≤ n-1) với bubble sort (bằng số
# nghịch thế). Giải thích sự chênh lệch.
# Ví dụ: selection thường ít swap hơn bubble

def selectionSort(arr,n):
    swap = 0
    arr_ = arr.copy()
    for i in range(n-1):
        min_pos = i
        for j in range(i+1,n):
            if arr_[j] < arr_[min_pos]:
                min_pos = j
        if arr_[i] != arr_[min_pos]:
            swap +=1
            arr_[i], arr_[min_pos] = arr_[min_pos], arr_[i]
    return swap

def bubbleSort(arr,n):
    swap = 0
    arr_ = arr.copy()
    for i in range(n-1):
        for j in range(n-i-1):
            if arr_[j] > arr_[j+1]:
                swap +=1
                arr_[j], arr_[j+1] = arr_[j+1], arr_[j]
    return swap

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                print(f'Selection Sort: {selectionSort(arr,n)} swap')
                print(f'Bubble Sort: {bubbleSort(arr,n)} swap')
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')
# selection thường ít swap hơn bubble vì selection sort chỉ hoán đổi vị trí của phần tử bé nhất còn
# bubble sort sẽ liên tục hoán đổi vị trí của phần tử cho đến khi phần tử lớn nhất nằm ở cuối mảng
