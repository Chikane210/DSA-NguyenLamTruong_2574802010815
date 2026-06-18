# Bài 8. Trạng thái sau k bước
# Cho mảng và k. Thực hiện k vòng chèn đầu tiên rồi in mảng. (Lưu ý: chỉ k+1 phần tử đầu
# được đảm bảo sắp xếp.)
# Ví dụ: a = [4, 3, 2, 1], k = 1 → [3, 4, 2, 1]

def k_insertionSort(arr,k):
    for i in range (1,k+1):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            k = int(input('k: '))
            if len(arr) > 0:
                print(k_insertionSort(arr,k))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')