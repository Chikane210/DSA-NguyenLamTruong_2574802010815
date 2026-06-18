# Bài 17. Phần tử nhỏ thứ k (partial selection)
# Tìm giá trị nhỏ thứ k mà không sắp xếp toàn bộ: chỉ chạy k vòng selection. Phân tích độ
# phức tạp O(n·k).
# Ví dụ: a = [7, 2, 5, 1, 9], k = 3 → 5

def partial_selection(arr,k,n):
    for i in range(k):
        min_pos = i
        for j in range(i+1,n):
            if arr[j] < arr[min_pos]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return arr[k-1]

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            k = int(input('k: '))
            n = len(arr)
            if n > 0:
                print(partial_selection(arr,k,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')
        
                