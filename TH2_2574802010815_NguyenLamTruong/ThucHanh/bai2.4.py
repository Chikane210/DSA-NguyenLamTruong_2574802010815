def binarySearch(arr,key,n):
    left = 0
    right = n -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            right = mid -1
        else:
            left = mid +1
    return -1
        
if __name__ == '__main__':
    while True:
        try:
            arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
            key = int(input())
            n = len(arr)
            if n > 0:
                binary_search = binarySearch(arr, key, n)
                if binary_search == -1:
                    print('Khong tim thay phan tu trong mang')
                else:
                    print(binary_search)
                    break
            else:
                print('mang rong')
        except ValueError:
            print('Dinh dang dau vao khong hop le!')