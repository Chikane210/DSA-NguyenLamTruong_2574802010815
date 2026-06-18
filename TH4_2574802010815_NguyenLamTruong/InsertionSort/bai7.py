# Bài 7. Sắp xếp mảng ký tự
# Dùng insertion sort sắp xếp một mảng ký tự theo bảng chữ cái.
# Ví dụ: a = ['d','a','c','b'] → ['a','b','c','d']

def insertionSort_word(arr,n):
    for i in range (1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    while True:
        arr = [x for x in input().split()]
        n = len(arr)
        if len(arr) > 0:
            print(insertionSort_word(arr,n))
            break
        print('mang rong')
