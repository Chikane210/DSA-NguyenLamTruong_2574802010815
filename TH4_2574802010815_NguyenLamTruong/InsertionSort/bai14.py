# Bài 14. Sắp xếp đối tượng theo nhiều khóa
# Sắp danh sách học sinh theo điểm giảm dần, nếu bằng điểm thì theo tên tăng dần.
# Ví dụ: [('Cu',8),('Ba',9),('An',8)] → [('Ba',9),('An',8),('Cu',8)]
def insertionSort_for_keys(arr,n):
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and (arr[j][1] < key[1] or (arr[j][1] == key[1] and arr[j][0] > key[0])):
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    while True:
        try:
            arr = [('Cu',8),('Ba',9),('An',8)]
            n = len(arr)
            if n > 0:
                print(insertionSort_for_keys(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')