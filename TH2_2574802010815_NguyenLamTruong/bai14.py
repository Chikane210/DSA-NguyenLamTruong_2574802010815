# Bài 14. Tìm trong ma trận 2D
# Ma trận m×n: mỗi hàng tăng dần và phần tử đầu mỗi hàng > phần tử cuối hàng trước. Tìm x.
# Ví dụ: [[1,3,5],[7,9,11]], x = 9 → true
    
def matrix_2D(matrix, key):
    for arr in matrix:
        n = len(arr)
        left = 0
        right = n-1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == key:
                return True
            elif arr[mid] > key:
                right = mid -1
            else:
                left = mid +1
    return False

def create_matrix_2D():
    print('tao ma tran 2D')
    matrix = []
    for i in range(2):
        while True:
            try:
                arr = [int(x) for x in input().split()]
                if len(arr) > 0:
                    matrix.append(sorted(arr))
                    break
                print('mang rong')
            except ValueError:
                print('nhap so nguyen')
    return matrix

if __name__ == '__main__':
    matrix = create_matrix_2D()
    while True:
        try:
            key = int(input())
            break
        except ValueError:
            print('dinh dang dau voa khong hop le')
    print(matrix_2D(matrix, key))