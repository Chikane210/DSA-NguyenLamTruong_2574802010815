# Bài 9. Binary insertion sort
# Cải tiến: dùng tìm kiếm nhị phân để xác định vị trí chèn (giảm số so sánh xuống O(log i)),
# sau đó vẫn dịch chuyển để chèn. Đếm số so sánh và so với bản thường.
# Ví dụ: giảm số so sánh nhưng số shift không đổi

def Binary_insertion_sort(arr,n):
    left = 0
    right = n-1
    while left <= right:
        mid = (left + right) // 2
        