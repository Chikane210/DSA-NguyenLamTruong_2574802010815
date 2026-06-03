def binary_search(arr, key): #Tạo một hàm tìm kiếm nhị phân với tham số truyền vào là một mảng và phần tử cần tìm
    mid = 0 #Khởi tạo biến chỉ sô ở giữa mảng
    left = 0
    right = len(arr) -1
    step = 0
    while (left <= right): #Vòng lặp tiếp tục khi khoảng tìm kiếm hợp lệ
        step = step+1
        mid = (left + right) // 2
        if (key == arr[mid]): #nếu tìm thấy phần tử key ở vị trí mid -> return vị trí phần tử
            return mid
        if (key < arr[mid]): #nếu phần tử key bé hơn vị trí mid -> dịch mid về phía bên phải
            right = mid - 1
        else:
            left = mid + 1
    return -1
arr = [0, 4, 5, 9, 13, 15, 18, 24, 28, 29, 35]
key = 40
result = binary_search(arr, key)
print("Vi tri tim kiem thu i la:", result)
#Nhan xet: input & output cua Giai thuat Nhị phân ??
# input: arr = [0, 4, 5, 9, 13, 15, 18, 24, 28, 29, 35]
# output: -1 (phần tử cần tìm không xuất hiện trong mảng)
#Yêu cầu – comment vào dấu note, bước lặp, vòng lặp của giải thuật