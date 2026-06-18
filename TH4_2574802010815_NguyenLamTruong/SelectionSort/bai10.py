# Bài 10. Đếm chính xác số swap
# Chỉ hoán đổi khi phần tử nhỏ nhất khác vị trí hiện tại. Đếm số swap thực sự xảy ra.
# Ví dụ: a = [1, 2, 3] → 0 swap

def count_true_swap(arr,n):
    swap = 0
    for i in range(n-1):
        min_pos = i
        for j in range(i+1,n):
            if arr[j] < arr[min_pos]:
                min_pos = j
        if arr[min_pos] != arr[i]:
            swap +=1
            arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return swap

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                print(f'{arr} -> {count_true_swap(arr,n)} swap ')
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')