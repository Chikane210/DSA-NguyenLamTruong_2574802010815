def binary_search(array, element):
    mid = 0
    start = 0
    end = len(array) -1
    step = 0
    while (start <= end):
        step = step+1
        mid = (start + end) // 2
        if element == array[mid]:
            return mid
        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1
array = [0, 4, 5, 9, 13, 15, 18, 24, 28, 29, 35]
element = 28
result = binary_search(array, element)
print("Phan tu tim kiem duoc la:", result)

#Nhận xét: input & output cua Giai thuat ??
#input: [0, 4, 5, 9, 13, 15, 18, 24, 28, 29, 35]
#output: 8