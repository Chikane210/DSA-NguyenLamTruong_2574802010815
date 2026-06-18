# Bài 23. Phân tích best / average / worst
# Phân tích số so sánh và swap trên 3 đầu vào: đã sắp xếp, ngẫu nhiên, sắp xếp ngược. Chỉ ra
# selection sort luôn O(n²) so sánh nhưng số swap thì khác nhau.
# Ví dụ: so sánh luôn O(n²); swap: 0 đến n-1
from random import randint
def selectioSort(arr,n):
    swap = 0
    compare = 0
    for i in range(n-1):
        min_pos = i
        for j in range(i+1,n):
            compare +=1
            if arr[j] < arr[min_pos]:
                min_pos = j
        if arr[i] != arr[min_pos]:
            swap +=1
            arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return swap, compare

if __name__ == '__main__':
    while True:
        try:
            n = int(input('n: '))
            if n > 0:
                randomElement_arr = [randint(0,n) for x in range(0,n)]
                sorted_arr = list(range(0,n))
                reverse_arr = list(range(0,n))[::-1]
                
                swap1,compare1 = selectioSort(randomElement_arr, n)
                swap2, compare2 = selectioSort(sorted_arr,n)
                swap3, compare3 = selectioSort(reverse_arr,n)
                
                print(f'Mang ngau nhien: {swap1} swap | {compare1} compare ')
                print(f'Mang da sap xep: {swap2} swap | {compare2}')
                print(f'Mang nguoc: {swap3} swap | {compare3} compare')
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')