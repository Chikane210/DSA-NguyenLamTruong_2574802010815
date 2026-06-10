# Sắp xếp danh sách học sinh theo điểm giảm dần, nếu bằng điểm thì theo tên tăng dần
# (tận dụng tính ổn định của bubble sort).
# Ví dụ: [('An',8),('Ba',9),('Cu',8)] → [('Ba',9),('An',8),('Cu',8)]

def sap_xep_diem(arr,n):
    for i in range (n-1):
        for j in range (n-i-1):
            if arr[j][1] < arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            elif arr[j][1] == arr[j+1][1] and arr[j][0] > arr[j+1][0]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [('Minh', 7), ('An', 9), ('Cu', 7), ('Ba', 9), ('Duc', 7)]
n = len(arr)
print(sap_xep_diem(arr, n))
