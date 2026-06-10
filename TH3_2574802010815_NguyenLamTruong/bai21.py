# Bài 21. Sắp xếp ổn định theo cặp (key, value)
# Cho dãy bản ghi, yêu cầu sắp theo key tăng dần nhưng bắt buộc ổn định; viết test chứng
# minh kết quả khác với một thuật toán không ổn định trên cùng dữ liệu.
# Ví dụ: kiểm chứng tính ổn định bằng nhãn phân biệt

def bubbleSort_couple(arr,n):
    for i in range(n-1):
        swapped =False
        for j in range(n-i-1):
            if arr[j]['gia'] > arr[j+1]['gia']:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            return arr

def selectionSort_couple(arr,n):
    for i in range (n):
        min_pos = i
        for j in range(i+1, n):
            if arr[j]['gia'] < arr[min_pos]['gia']:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]  
    return arr

if __name__ == '__main__':     
    arr = [
        {"id": 101, "ten": "Chuột không dây", "gia": 250000},
        {"id": 102, "ten": "Bàn phím cơ", "gia": 850000},
        {"id": 103, "ten": "Tai nghe Gaming", "gia": 500000}
    ]
    n = len(arr)
    arr_bb = arr.copy()
    arr_sl = arr.copy()
    if n > 0:
        print('Bubble Sort')
        bubbleSort_result = bubbleSort_couple(arr_bb, n)
        for i in bubbleSort_result:
            print(i)
        print('Selection Sort')
        selectionSort_result = selectionSort_couple(arr_sl,n)
        for i in selectionSort_result:
            print(i)
