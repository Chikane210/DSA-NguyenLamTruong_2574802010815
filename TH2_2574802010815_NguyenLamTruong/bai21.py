# Bài 21. Chia mảng tổng lớn nhất nhỏ nhất (Split Array Largest Sum)
# Chia mảng thành k đoạn liên tiếp không rỗng sao cho tổng lớn nhất trong các đoạn là
# nhỏ nhất. Trả về tổng đó.
# Ví dụ: a = [7,2,5,10,8], k = 2 → 18 (chia [7,2,5] và [10,8])

def ktr_doan(arr, k, doan, n):
    so_doan = 1
    doan_ht = arr[0]
    for i in range(1,n):
        if arr[i] + doan_ht > doan:
            so_doan += 1
            doan_ht = arr[i]
        else:
            doan_ht += arr[i]
    if so_doan <= k:
        return True
    return False

def chia_mang(arr, k, n):
    left = arr[-1]
    right = sum(arr)
    result = 0
    while left <= right:
        mid = (left + right) // 2
        check = ktr_doan(arr,k,mid,n)
        if check == True:
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
            k = int(input('k: '))
            if n > 0:
                arr_sort = sorted(arr)                
                print(chia_mang(arr_sort, k, n))
                break
            else:
                print('mang rong')
        except ValueError:
            print('Dinh dang dau vao khong hop le')