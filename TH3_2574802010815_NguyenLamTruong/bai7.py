# Bài 7. Sắp xếp mảng ký tự
# Dùng bubble sort sắp xếp một mảng ký tự theo thứ tự bảng chữ cái.
# Ví dụ: a = ['d','a','c','b'] → ['a','b','c','d']

def bubbleSort_word(arr,n):
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr

if __name__ == '__main__':
    while True:
        arr = [x for x in input().split()]
        n = len(arr)
        if n > 0:
            print(bubbleSort_word(arr,n))
            break
        print('mang rong')