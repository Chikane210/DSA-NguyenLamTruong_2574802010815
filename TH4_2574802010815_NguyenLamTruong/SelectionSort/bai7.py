# Bài 7. Sắp xếp mảng ký tự
# Dùng selection sort sắp xếp một mảng ký tự theo bảng chữ cái.
# Ví dụ: a = ['d','a','c','b'] → ['a','b','c','d']

def selectionSort_word(arr,n):
    for i in range(n-1):
        min_pos = i
        for j in range(i+1,n):
            if arr[j] < arr[min_pos]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return arr

if __name__ == '__main__':
    while True:
        arr = [x for x in input().split()]
        n = len(arr)
        if n > 0:
            print(selectionSort_word(arr,n))
            break
        print('mang rong')
