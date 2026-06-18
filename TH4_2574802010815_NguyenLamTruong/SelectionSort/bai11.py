# Đưa ra ví dụ cho thấy selection sort không ổn định: hai phần tử cùng khóa bị đảo thứ tự sau
# khi sắp xếp.
# Ví dụ: [(2,'a'),(2,'b'),(1,'c')] có thể đổi thứ tự a,b

def selectionSort_unstable(arr,n):
    for i in range (n-1):
        min_pos = i
        for j in range(i+1,n):
            if arr[j][0] < arr[min_pos][0]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return arr

if __name__ == '__main__':
    while True:
        arr = [(2,'a'),(2,'b'),(1,'c')]
        n = len(arr)
        if n > 0:
            print(selectionSort_unstable(arr,n))
            break
        print('mang rong')