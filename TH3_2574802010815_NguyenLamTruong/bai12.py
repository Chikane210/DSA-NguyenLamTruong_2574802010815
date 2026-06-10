# Bài 12. Sắp xếp chuỗi theo độ dài
# Dùng bubble sort sắp xếp danh sách chuỗi tăng dần theo độ dài.
# Ví dụ: a = ['abc','a','ab'] → ['a','ab','abc']

def bubbleSort_string(arr,n):
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if len(arr[j]) > len(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped == True
        if swapped == False:
            return arr

if __name__ == '__main__':
    while True:
        arr = [x for x in input().split()]
        n = len(arr)
        if n > 0:
            print(bubbleSort_string(arr,n))
            break
        print('mang rong')