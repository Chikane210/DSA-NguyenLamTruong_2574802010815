# Bài 13. Tính ổn định (stability)
# Chứng tỏ insertion sort ổn định: sắp danh sách cặp (khóa, nhãn) theo khóa và kiểm tra phần
# tử cùng khóa giữ nguyên thứ tự ban đầu.
# Ví dụ: [(2,'a'),(1,'b'),(2,'c')] → [(1,'b'),(2,'a'),(2,'c')]

def stability_insertionSort(arr,n):
    for i in range (1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j][0] > key[0]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    while True:
        try:
            arr = [(2,'b'),(2,'a'),(2,'c')]
            n = len(arr)
            if n > 0:
                print(stability_insertionSort(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')