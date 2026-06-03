# Bài 20. Chia sách cho học sinh (Book Allocation)
# Có n cuốn sách số trang p[i], chia cho m học sinh sao cho mỗi học sinh nhận các cuốn liên
# tiếp và số trang tối đa của một học sinh là nhỏ nhất. Tìm giá trị đó.
# Ví dụ: p = [12,34,67,90], m = 2 → 113

def ktr_hs(arr, hs, so_trang, n):
    so_hs = 1
    trang_ht = arr[0]
    for p in range(1,n):
        if arr[p] + trang_ht > so_trang:
            so_hs +=1
            trang_ht = arr[p]
        else:
            trang_ht += arr[p]
    if so_hs <= hs:
        return True
    return False

def chia_sach(arr, hs, n):
    left = arr[-1]
    right = sum(arr)
    result = 0
    while left <= right:
        mid = (left + right) // 2
        check = ktr_hs(arr, hs, so_trang=mid, n=n)
        if check ==  True:
            result = mid
            right = mid -1
        else:
            left = mid +1
    return result

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            hs = int(input('m: '))
            if n > 0:
                arr_sort = sorted(arr)
                print(chia_sach(arr_sort, hs, n))
                break
            else:
                print('mang rong')
        except ValueError:
            print('Dinh dang dau vao khong hop le')