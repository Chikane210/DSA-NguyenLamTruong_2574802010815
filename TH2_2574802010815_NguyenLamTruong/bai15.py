# Bài 15. K phần tử gần nhất (K Closest Elements)
# Mảng đã sắp xếp. Tìm k phần tử gần x nhất, trả về theo thứ tự tăng dần.
# Ví dụ: a = [1,2,3,4,5], k = 4, x = 3 → [1,2,3,4]

def find_closetElement(arr, k, x, n):
    left = 0
    right = n -1
    while left <= right:
        mid = (left + right) // 2
        mid_index = mid
        if arr[mid] == x:
            break
        elif arr[mid] < x:
            left = mid +1
        else:
            right = mid -1

    left_site = []
    for i in range (0, mid_index +1):
        distance = x- arr[i]
        left_site.append([distance, arr[i]])
    right_site = []
    for i in range (mid_index +1, n):
        distance = arr[i] -x
        right_site.append([distance, arr[i]])
    distance_arr = left_site + right_site
    distance_arr.sort()
    
    result = []
    for i in range(k):
        result.append(distance_arr[i][1])
    return result

if __name__ == '__main__':
    while True:
        try:
            arr = [int(x) for x in input().split()]
            n = len(arr)
            x = int(input('x: '))
            k = int(input('k: '))
            if n > 0:
                K_closet_element = sorted(find_closetElement(arr, k, x, n))
                print(K_closet_element)
                break
            else:
                print('mang rong')
        except ValueError:
            print('Dinh dang dau vao khong hop le')

        
    