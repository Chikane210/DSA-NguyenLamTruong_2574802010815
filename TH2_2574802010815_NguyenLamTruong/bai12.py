# Bài 12. Tìm đỉnh (Peak Element)
# Phần tử "đỉnh" lớn hơn cả hai hàng xóm. Trả về chỉ số một đỉnh bất kỳ. Coi a[-1] = a[n] = âm
# vô cực.
# Ví dụ: a = [1, 2, 3, 1] → 2

def peakElement(arr,n):
    left = 0
    right = n -1
    peak = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid +1]:
            left = mid +1
        else:
            peak = mid
            right = mid -1
    return peak

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                print(peakElement(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')
            