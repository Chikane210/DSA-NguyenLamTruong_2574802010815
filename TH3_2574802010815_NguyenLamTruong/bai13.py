# Bài 13. Tính ổn định (stability)
# Chứng tỏ bubble sort ổn định: cho mảng cặp (khóa, nhãn), sắp xếp theo khóa và kiểm tra
# các phần tử cùng khóa giữ nguyên thứ tự ban đầu.
# Ví dụ: [(2,'a'),(1,'b'),(2,'c')] → [(1,'b'),(2,'a'),(2,'c')]

def stability_bubbleSort(arr,n):
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j][0] > arr[j+1][0]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            return arr

if __name__ == '__main__':
    while True:
        try:
            arr = [(2,'a'), (1,'b'), (2,'c'), [5, 'a'], (4,'b')]
            n = len(arr)
            if n > 0:
                print(stability_bubbleSort(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap vao so nguyen')