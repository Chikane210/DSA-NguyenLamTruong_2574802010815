# Bài 13. Sắp xếp đối tượng theo khóa
# Sắp danh sách học sinh theo điểm tăng dần bằng selection sort.
# Ví dụ: [('An',8),('Ba',5)] → [('Ba',5),('An',8)]

def sortObject_for_key(arr,n):
    for i in range(n-1):
        min_pos = i
        for j in range(i+1,n):
            if arr[j][1] < arr[min_pos][1]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return arr

if __name__ == '__main__':
    while True:
        arr = [('An',8),('Ba',5),('Cu',7)]
        n = len(arr)
        if n > 0:
            print(sortObject_for_key(arr,n))
            break
        print('mang rong')