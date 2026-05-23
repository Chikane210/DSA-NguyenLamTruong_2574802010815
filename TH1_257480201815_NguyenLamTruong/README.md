Bài 1. Bằng lời của bạn, hãy mô tả ý tưởng của thuật toán tìm kiếm tuyến tính. Nêu rõ Input và
Output của thuật toán, và cho biết thuật toán dừng lại trong những trường hợp nào.

-Input: mảng gồm N phần tử, từ khóa (phần tử cần tìm)
-Sử dụng vòng lặp (for or while) để duyệt lần lượt các phần tử trong mảng
-Kiểm tra xem phần tử ở vị trí đang duyệt có giá trị bằng với từ khóa không. Nếu có xuất ra phần tử or vị trí phần tử đó và dừng vòng lặp, ngược lại thì tiếp tục duyệt các phần tử cho đến khi tìm thấy phần tử cần tìm hoặc duyệt hết mảng
-Output: thông báo kết quả phần tử cần tìm có trong mảng hay không

Bài 2. Cho mảng A = [7, 3, 9, 12, 5, 8, 1] và x = 5. Hãy lập bảng mô phỏng từng bước: ở mỗi bước
ghi rõ chỉ số i, giá trị A[i], kết quả so sánh A[i] với x, và kết luận. Cuối cùng cho biết giá trị mà
hàm trả về.

i = 0
A[0] = 7 != x = 5
i = 0 + 1

i = 1
A[1] = 3 != x = 5
i = 1 + 1

i = 2
A[2] = 9 != x = 5
i = 2 + 1

i = 3
A[3] = 12 != x = 5
i = 3 + 1

i = 4
A[4] = 5 = x = 5
=> Phần tử đang tìm ở vị trí i = 4
Giá trị hàm trả về: 4

Bài 3. Vẫn với mảng A ở Bài 2, hãy đếm số phép so sánh (A[i] == x) cần thực hiện để tìm: (a) x = 7;
(b) x = 1; (c) x = 100 (không có trong mảng). Em rút ra nhận xét gì về vị trí của phần tử và
số phép so sánh?

-Số phép so sánh để tìm (a) x = 7: 1
                        (b) x = 1: 7
                        (c) x = 100: 7
=> Vị trí phần tử = số phép so sánh - 1

Bài 4. Một mảng có n phần tử. Hãy cho biết số phép so sánh trong: (a) trường hợp tốt nhất; (b)
trường hợp xấu nhất; (c) trung bình (khi phần tử có trong mảng). Từ đó suy ra độ phức tạp
thời gian của thuật toán theo ký hiệu O lớn.

-Trường hợp (a): vị trí phần tử cần tìm ở đầu mảng 
-Trường hợp (b): vị trí phần tử cần tìm ở cuối mảng hoặc không xuất hiện trong mảng
-Trường hợp (c): vị trí phần tử cần tìm ở những vị trí khác 2 trường hợp trên
=> Độ phức tạp thời gian phụ thuộc vào vị trí phần tử: O(n)

Bài 5. Tìm kiếm tuyến tính có bắt buộc mảng phải được sắp xếp trước hay không? Giải thích. So
sánh ngắn gọn với tìm kiếm nhị phân về: điều kiện áp dụng và độ phức tạp.

-Tìm kiếm tuyến tính không bắt buộc mảng phải được sắp xếp trước. Vì kỹ thuật này chỉ duyệt qua lần lượt các phần tử xuất hiện trong mảng và so sánh phần tử đang duyệt với từ khóa
-Tìm kiếm tuyến tính: không yêu cầu mảng cần được sắp xếp, độ phức tạp: O(n)
-Tìm kiếm nhị phân: yêu cầu mảng được sắp xếp (lớn-bé, bé-lớn), độ phức tạp O(log 2n)