# Bài 24. Khôi phục số swap từ hai trạng thái
# Cho mảng ban đầu và mảng sau một số lượt bubble sort chưa hoàn tất. Xác định đã thực
# hiện ít nhất bao nhiêu lượt để đi từ trạng thái đầu đến trạng thái sau.
# Ví dụ: đầu = [4,3,2,1], sau = [3,2,1,4] → 1 lượt
    
def backup_swap_number(arr,final_arr,n):
    turn = 0
    if arr == final_arr:
        return turn
    for i in range(n-1):
        turn +=1
        for j in range (n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if arr == final_arr:
            return turn

def k_bubbleSort(arr,k,n):
    for i in range(k):
        flag = False
        for j in range (n-i-1):
            if arr[j] > arr[j+1]:
                flag = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
    if flag == False:
        return arr
    return arr
 
if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            k = int(input('k: '))
            n = len(arr)
            if n > 0:
                arr_ = arr.copy()
                mang_sapxep_chua_hoan_tat = k_bubbleSort(arr_, k, n)
                print(backup_swap_number(arr, mang_sapxep_chua_hoan_tat, n))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen') 


        