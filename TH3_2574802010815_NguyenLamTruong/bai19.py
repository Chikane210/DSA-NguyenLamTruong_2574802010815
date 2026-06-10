# Bài 19. Số lượt tối thiểu cho mảng gần sắp xếp
# Với bản early-exit, tìm số lượt tối thiểu cần thiết. Liên hệ kết quả với khoảng cách xa nhất
# mà một phần tử phải "đi ngược" về vị trí đúng.
# Ví dụ: a = [1, 2, 3, 5, 4] → 1 lượt


def luot_toi_thieu(arr,n):
    turn = 0
    for i in range(n-1):
        swapped = False
        turn +=1
        for j in range (n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
        if swapped == False:
            return turn
   
def right_pos(arr,n):
    arr.sort()
    vitri=[]
    for index in range(n):
        vitri.append((arr[index], index))
    return vitri

def present_pos(arr,n):
    vitri = []
    for index in range(n):
        vitri.append((arr[index], index))
    return vitri

def kc_dinguoc_xa_nhat(arr,n):
    vitri_dung = right_pos(arr,n)
    vitri_ht = present_pos(arr,n)
    di_nguoc_xa_nhat = 0
    for i in arr:
        for j in range(n):
            di_nguoc = vitri_ht[j][1] - vitri_dung[j][1]
            if di_nguoc > di_nguoc_xa_nhat:
                di_nguoc_xa_nhat = di_nguoc
    return di_nguoc_xa_nhat + 1
            

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                print('Turn: ',luot_toi_thieu(arr,n))
                print('Khoang cach di nguoc xa nhat',kc_dinguoc_xa_nhat(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap vao so nguyen')