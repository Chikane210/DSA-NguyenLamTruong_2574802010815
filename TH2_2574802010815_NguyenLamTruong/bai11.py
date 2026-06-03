# Bài 11. Phần tử nhỏ nhất trong mảng xoay
# Mảng sắp xếp bị xoay (không trùng). Tìm giá trị nhỏ nhất.
# Ví dụ: a = [3, 4, 5, 1, 2] → 1

def find_minElement(arr, n):
    left = 0
    right = n -1
    min_element = arr[0]
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid +1
        else:
            if arr[mid] < min_element:
                min_element = arr[mid]
            right = mid -1
    return min_element

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                print(find_minElement(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')
            
            
            
            
