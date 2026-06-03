# Bài 8. Căn bậc hai nguyên
# Cho số nguyên không âm n, trả về phần nguyên của căn bậc hai của n không dùng hàm
# sqrt.
# Ví dụ: n = 8 → 2 ; n = 16 → 4

def canbac2_nguyen(n):
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        if mid**2 == n:
            return mid
        elif mid**2 < n:
            result = mid
            left = mid +1
        else:
            right = mid -1
    return result

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            if n >= 0:
                print(canbac2_nguyen(n))
                break
            print('so nguyen lon hon 0')
        except ValueError:
            print('nhap vao so nguyen duong')