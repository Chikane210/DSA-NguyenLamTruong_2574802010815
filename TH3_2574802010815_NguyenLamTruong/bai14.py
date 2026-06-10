# Bài 14. Cocktail shaker sort
# Cài đặt bubble sort hai chiều: mỗi vòng đẩy phần tử lớn nhất về cuối rồi đẩy phần tử nhỏ nhất
# về đầu. So sánh số lượt với bubble sort thường trên cùng mảng.
# Ví dụ: a = [5, 1, 4, 2, 8] → [1, 2, 4, 5, 8]

def cocktail_shakerSort(arr,n):
    turn = 0
    start = 0
    for i in range(n-1):
        swapped = False
        turn += 1
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swapped = True
        for j in range (n-i-1, start, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swapped = True
            start += 1
        if swapped == False:
            break
    return arr, turn

def bubbleSort(arr, n):
    turn = 0
    for i in range (n-1):
        swapped = False
        turn +=1 
        for j in range (n-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swapped = True
        if swapped == False:
            break
    return arr, turn 

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            arr_cocktail = arr.copy()
            arr_bubble = arr.copy()
            if n > 0:
                cocktail_shake, cocktail_turn = cocktail_shakerSort(arr_cocktail,n)
                bubble_sort, bubble_turn = bubbleSort(arr_bubble,n)
                print(f'Cocktail Shake Sort: {cocktail_shake}, Turn: {cocktail_turn}')
                print(f'Bubble Sort: {bubble_sort}, Turn: {bubble_turn}')
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')
