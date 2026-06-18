# Bài 1. Tìm phần tử nhỏ nhất đưa về đầu
# Cho mảng a. Tìm phần tử nhỏ nhất và hoán đổi nó về vị trí đầu tiên (một bước đầu của
# selection sort).
# Ví dụ: a = [4, 2, 7, 1, 3] → [1, 2, 7, 4, 3]

def oneStep_selectionSort(arr,n):
    min_pos = 0
    for i in range(0,n-1):
        if arr[i] < arr[min_pos]:
            min_pos = i
    arr[0], arr[min_pos] = arr[min_pos], arr[0]
    return arr

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            if n > 0:
                print(oneStep_selectionSort(arr,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')