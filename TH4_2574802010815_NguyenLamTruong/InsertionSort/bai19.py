# Bài 19. Gnome sort
# Cài đặt gnome sort — một biến thể đơn giản của insertion sort dùng một con trỏ tiến/lùi
# thay cho vòng lặp lồng. So sánh số thao tác với insertion sort.
# Ví dụ: a = [3, 2, 1] → [1, 2, 3]
def gnomeSort(arr, n):
    pos = 0
    count = 0
    while pos < n:
        count +=1    
        if pos == 0 or arr[pos] >= arr[pos-1]:
            pos+=1
        else:
            arr[pos], arr[pos-1] = arr[pos-1], arr[pos]
            pos -=1
    return arr,count

def insertionSort(arr, n):
    compare = 0
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0:
            compare +=1
            if arr[j] > key:
                arr[j+1] = arr[j]
                j -=1
            else:
                break
        arr[j+1] = key
    return arr, compare

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if len(arr) > 0:
                arr_1 = arr.copy()
                arr_2 = arr.copy()
                sorted_1, count = gnomeSort(arr_1,n)
                sorted_2, compare = insertionSort(arr_2,n)
                print(f'GnomeSort: {arr_1} -> {count}')
                print(f'InsertinSort: {arr_2} -> {compare}')
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')