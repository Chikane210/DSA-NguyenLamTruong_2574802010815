# Bài 16. Koko ăn chuối (Binary search trên đáp án)
# Có n đống chuối, đống i có pile[i] quả. Koko ăn s quả/giờ (ăn hết 1 đống/giờ kể cả còn dư).
# Tìm tốc độ s nhỏ nhất để ăn xong trong h giờ.
# Ví dụ: pile = [3,6,7,11], h = 8 → 4

def tg_an_chuoi(pile, s):
    tong_gio = 0
    for banana in pile:
        tong_gio += (banana +s -1) // s
    return tong_gio

def koko_eating_banana(pile, h):
    left = 1
    right = pile[-1]
    s_min = 0
    while left <= right:
        mid = (left + right) // 2
        time = tg_an_chuoi(pile, mid) 
        if time > h:
            left = mid +1
        else:
            s_min = mid
            right = mid -1
    return s_min

if __name__ == '__main__':
    while True:
        try:
            piles = [int(x) for x in input().split()]
            h = int(input('Thoi gian quy dinh: '))
            if len(piles) > 0:
                sort_piles = sorted(piles)
                print('s =',koko_eating_banana(sort_piles, h))
                break
            print('ko co chuoi cho koko=(((')
        except ValueError:
            print('so luong chuoi phai la so nguyen')