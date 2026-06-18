# Bài 12. Sắp xếp chuỗi theo độ dài
# Dùng insertion sort sắp xếp danh sách chuỗi tăng dần theo độ dài.
# Ví dụ: a = ['abc','a','ab'] → ['a','ab','abc']

def stringlen_insertionSort(arr, n):
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and len(arr[j]) > len(key):
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    while True:
        arr = [x for x in input().split()]
        n = len(arr)
        if len(arr) > 0:
            print(stringlen_insertionSort(arr,n))
            break
        print('mang rong')