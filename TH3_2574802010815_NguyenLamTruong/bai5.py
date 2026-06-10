# Bài 5. Đếm số lần so sánh
# Sắp xếp tăng dần và đếm tổng số lần so sánh hai phần tử (không tính swap).
# Ví dụ: a = [1, 2, 3] (chưa tối ưu) → 3 lần so sánh

def dem_lan_sosanh(arr,n):
    count = 0
    for i in range (n-1):
        for j in range (n-i-1):
            count += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return count

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                print(dem_lan_sosanh(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap vao so nguyen')