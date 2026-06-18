# Bài 22. Selection sort ổn định in-place
# Thử thách: làm selection sort vừa ổn định vừa không tốn thêm bộ nhớ đáng kể. Thảo
# luận vì sao điều này khó và đánh đổi với số thao tác dịch chuyển.
# Ví dụ: phân tích đánh đổi stability vs số shift

def selectionSort_stable_inplace(arr_,n):
    shift = 0
    compare = 0
    arr = arr_.copy()
    for i in range(n-1):
        min_pos = i
        for j in range(i+1,n):
            compare +=1
            if arr[j][0] < arr[min_pos][0]:
                min_pos = j
        key = arr[min_pos]
        while min_pos > i:
            shift +=1
            arr[min_pos] = arr[min_pos-1]
            min_pos -=1
        arr[i] = key
    return shift, compare
    
def selectionSort_unstable_inplace(arr_,n):
    swap = 0 
    compare = 0
    arr= arr_.copy()
    for i in range(n-1):
        min_pos = i
        for j in range(i+1,n):
            compare +=1
            if arr[j][0] < arr[min_pos][0]:
                min_pos = j
        if arr[min_pos] != arr[i]:
            swap +=1
            arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return swap, compare

if __name__ == '__main__':
    while True:
        try:
            arr = [(3, 'a'), (1, 'b'), (4, 'c'), (2, 'd'), (3, 'e'),
                   (1, 'f'), (5, 'g'), (2, 'h'), (4, 'i'), (3, 'j'),
                   (5, 'k'), (1, 'l'), (2, 'm'), (4, 'n'), (5, 'o'),
                   (3, 'p'), (1, 'q'), (2, 'r'), (4, 's'), (5, 't')  
                    ]
            n = len(arr)
            if n > 0:
                shift, compare1 = selectionSort_stable_inplace(arr,n)
                swap, compare2 = selectionSort_unstable_inplace(arr,n)
                print('---SELECTION SORT BAN ON DINH---')
                print(f'Shift: {shift} | Compare: {compare1}')
                print('---SELECTION SORT BAN THUONG (KHONG ON DINH)---')
                print(f'Swap: {swap} | Compare: {compare2}')
                break
            print('mang rong')
        except ValueError:
            print('nhap so nguyen')
#Việc số compare của cả 2 bằng nhau cho thấy dù bản ổn đinh hay không thì độ phức tạp của thuật toán vẫn là O(n^2).
#Tuy vậy để có sự ổn định thì thuật toán đẩy số lượng bộ nhớ lên rất nhiều khi so số shift (bản ổn định) vs số swap (bản thường)
#=> Để có được sự ổn định ta cần đánh đổi số thao tác lên nhiều so với bình thường