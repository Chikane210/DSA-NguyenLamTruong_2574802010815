# Bài 17. Sức chứa tàu hàng (Capacity To Ship Packages)                    
# Có n kiện hàng trọng lượng w[i], chuyển theo thứ tự trong D ngày. Tìm sức chứa tàu nhỏ                    
# nhất để hoàn thành trong D ngày.                  
# Ví dụ: w = [1,2,3,4,5,6,7,8,9,10], D = 5 → 15

def tinh_ngay(w, sc):
    ngay = 1
    trong_luong = 0
    for weight in w:
        if trong_luong + weight > sc:
            ngay += 1
            trong_luong = weight
        else:
            trong_luong += weight
    return ngay

def sc_tau(w, D):
    left = w[-1]
    right = sum(w)
    while left <= right:
        mid = (left + right) // 2 
        so_ngay = tinh_ngay(w,mid)
        if so_ngay > D:
            left = mid +1
        else:
            sc = mid
            right = mid -1
    return sc

if __name__ == '__main__':
    while True:
        try:
            w = [int(x) for x in input().split()]
            D = int(input('Thoi gian quy dinh: '))
            if len(w) > 0:
                sort_w = sorted(w)
                print(sc_tau(sort_w, D))
                break
            print('ko co kien hang')
        except ValueError:
            print('so luong hang phai la so nguyen')