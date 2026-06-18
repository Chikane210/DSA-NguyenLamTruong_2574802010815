Bài 25. Chứng minh tính đúng đắn (loop invariant)
Phát biểu và chứng minh bất biến vòng lặp: trước mỗi vòng lặp ngoài thứ i, đoạn a[0..i-1]
chứa đúng các phần tử ban đầu nhưng đã được sắp xếp. Suy ra thuật toán đúng.
Ví dụ: Bài chứng minh, không cần code

-Phát biểu bất biến vòng lặp
Trước khi bắt đầu vòng lặp ngoài ở bước i, đoạn mảng arr[0..i-1] chứa đúng các phần tử ban đầu của đoạn đó, nhưng đã được sắp xếp theo đúng thứ tự tăng dần

-Khởi tạo
Trước khi vòng lặp bắt đầu i = 1:Đoạn mảng được xét theo định nghĩa bất biến là arr[0..i-1] = arr[0..0]. Đoạn mảng này chỉ gồm duy nhất một phần tử arr[0] chính là phần tử ban đầu của nó. Một mảng chỉ có 1 phần tử thì hiển nhiên luôn luôn được coi là đã sắp xếp đúng thứ tự.

-Duy trì
Đoạn arr[0..i-1] đã gồm các phần tử ban đầu và đã được sắp xếp tăng dần. Thuật toán lấy phần tử key = a[i] và cơ chế vòng lặp trong sẽ dịch chuyển các phần tử lớn hơn key trong đoạn arr[0...i-1] sang phải để tạo khoảng trống rồi chèn key vào vị trí thích hợp vừa tạo. Sau khi kết thúc vòng lặp thứ i đoạn mảng arr[0..i] bây giờ bao gồm tất cả các phần tử cũ của đoạn arr[0..i-1] cộng thêm phần tử key vừa được chèn vào đúng vị trí
=>Đoạn arr[0..i] chứa đúng các phần tử ban đầu của nó và đã được sắp xếp theo thứ tự tăng dần.

-Thuật toán dừng
Vòng lặp ngoài được điều khiển bởi biến i tăng tuyến tính từ 1 -> n-1. Vì kích thước mảng n là hữu hạn, vòng lặp chắc chắn sẽ dừng sau khi thực hiện xong bước i = n-1.

-Chứng minh thuật toán dừng và đúng
Khi thuật toán kết thúc, vòng lặp ngoài vừa hoàn thành bước cuối cùng với i = n. Đoạn mảng arr[0..n-1] chứa đúng các phần tử ban đầu nhưng đã được sắp xếp theo thứ tự tăng dần. Vì đoạn arr[0..n-1]  chính là toàn bộ mảng ban đầu, điều này đồng nghĩa với việc toàn bộ mảng đã được sắp xếp thành công và không có phần tử nào bị mất mát hay thay đổi giá trị gốc.
