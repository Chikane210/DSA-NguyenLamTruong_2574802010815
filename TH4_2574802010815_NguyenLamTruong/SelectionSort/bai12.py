# Bài 12. Selection sort ổn định
# Sửa selection sort thành ổn định: thay vì swap, hãy dịch chuyển phần tử nhỏ nhất về vị trí
# đúng và đẩy phần còn lại. Kiểm chứng tính ổn định.
# Ví dụ: giữ nguyên thứ tự phần tử cùng khóa


def selectionSort_stable(arr,n):
    for i in range(n-1):
        min_pos = i
        for j in range(i+1,n):
            if arr[j] < arr[min_pos]:
                min_pos = j
        min_val = arr[min_pos]
        while min_pos > i:
            arr[min_pos] = arr[min_pos-1]
            min_pos -=1
        arr[i] = min_val
    return arr

if __name__ == '__main__':
    while True:
        arr = [(2,'a'),(2,'b'),(1,'c')]
        n = len(arr)
        if n > 0:
            print(selectionSort_stable(arr,n))
            break
        print('mang rong')