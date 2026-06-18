# Bài 15. Sắp xếp một phần (k nhỏ nhất)
# Chỉ cần k phần tử nhỏ nhất nằm đúng ở đầu. Thực hiện đúng k vòng selection và trả về mảng.
# Ví dụ: a = [5, 3, 1, 4, 2], k = 2 → [1, 2, ...]

def sort_a_part(arr,k,n):
    for i in range(k):
        min_pos = i
        for j in range(i+1,n):
            if arr[j] < arr[min_pos]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return arr

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            k = int(input('k: '))
            n = len(arr)
            if n > 0:
                print(sort_a_part(arr,k,n))
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')
        