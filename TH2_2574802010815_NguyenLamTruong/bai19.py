# Bài 19. Chia bò vào chuồng (Aggressive Cows)
# Có n chuồng tại vị trí x[i] và c con bò. Đặt bò sao cho khoảng cách nhỏ nhất giữa hai con bò
# bất kỳ là lớn nhất có thể. Tìm khoảng cách lớn nhất đó.
# Ví dụ: x = [1,2,4,8,9], c = 3 → 3 (đặt tại 1, 4, 8)

def ktr_bo(arr, cow, kc, n):
    vitri_bo = arr[0]
    so_luong = 1
    for i in range (1, n):
        if (arr[i] - vitri_bo) >= kc:
            so_luong +=1
            vitri_bo = arr[i]    
    if so_luong >= cow:
        return True
    return False

def chia_bo(arr, cow, n):
    left = 1
    right = arr[-1] - arr[0]
    result = 0
    while left <= right:
        mid = (left + right) // 2
        check = ktr_bo(arr=arr, cow=cow, kc=mid, n=n)
        if check == True:
            result = mid
            left = mid +1
        else:
            right = mid -1
    return result
            
if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            cow = int(input('cow: '))
            if n > 0:
                arr_sort = sorted(arr)
                print(chia_bo(arr_sort, cow, n))
                break
            else:
                print('mang rong')
        except ValueError:
            print('Dinh dang dau vao khong hop le')
