Bài 19. Double-ended selection — phân tích
Phân tích kỹ bản double selection (bài 9): số vòng, số so sánh, các trường hợp biên khi min và
max trùng vị trí hoán đổi. Chứng minh tính đúng đắn.
Ví dụ: xử lý cẩn thận khi maxIdx = vị trí đầu

1. Số vòng
-Sau mỗi vòng lặp ngoài phạm vi xét của mảng sẽ thu hẹp lại 2 phần tử => số vòng lặp tối đa = n//2
-Ở vòng lặp trong tại vòng lặp thứ i, phạm vi tìm kiếm Min/Max thu hẹp lại ở cả hai phía, chỉ xét từ chỉ số
i + 1 -> n - i - 1

2. Số lần so sánh
-Ở mỗi vòng lặp, xác định min_pos và max_pos
-Mỗi phần tử tốn 2 lần so sánh (một cho min, một cho max).

3. Trường hợp biên khi min và max trùng vị trí hoán đổi
-Trường hợp khi các phần tử trong phân đoạn đang xét có giá trị hoàn toàn (min_pos == max_pos), lúc này vòng lặp trong không tìm thấy phần tử nhỏ hơn, lớn hơn hẳn. => Vì tất cả các giá trị trong đoạn đều bằng nhau, việc đổi chỗ giữa đầu và cuối không làm ảnh hưởng đến mảng 

4. Chứng minh tính đúng đắn
-Trước khi bắt đầu vòng lặp - arr[0..i-1] đã được sắp xếp tăng dần, arr[n-i...n-1] đã được sắp xếp giảm dần và mọi
phần tử arr[i...n-i-1] đều lớn hơn hoặc bằng phần tử ở đoạn đầu, nhỏ hơn phần tử ở phần cuối

-Tính khởi đầu
Tại i = 0, các đoạn arr[0...-1] & arr[n..n-1] đều là tập hợp rỗng -> các điều kiện bất biến là đúng

-Tính duy trì
Tại bước đầu ở i, vòng lặp trong duyệt qua toàn bộ arr[i...n-i-1] để tìm ra min_pos & max_pos. Sau khi thực hiện phép hoán đổi thì chắc chắn min_pos sẽ đưa về vị trí i & max_pos sẽ đưa về vị trí n-i-1. Vì vậy, khi chuẩn bị bước sang vòng lặp i+1, hai phần tử arr[i] và arr[n-i-1] đã ổn định vị trí, kéo dãn phần biên đã sắp xếp thêm 1 phần tử ở mỗi đầu. Bất biến được duy trì.

-Tính kết thúc
Vòng lặp kết thúc khi i = n // 2. Nếu n chẵn, hai biên hội tụ khít nhau, toàn bộ mảng đã được duyệt và sắp xếp xong. Nếu n lẻ, hai biên hội tụ và chừa lại đúng 1 phần tử duy nhất ở chính giữa mảng. Theo tính chất 3 của bất biến, phần tử ở giữa này đã lớn hơn mọi phần tử bên trái và nhỏ hơn mọi phần tử bên phải, nên nó tự động đứng đúng vị trí mà không cần xử lý thêm.

--------------------------------------------------------------------------------------------------------------------

Bài 25. Chứng minh tính đúng đắn (loop invariant)
Phát biểu và chứng minh bất biến vòng lặp: sau vòng thứ i, đoạn a[0..i] chứa i+1 phần tử
nhỏ nhất của mảng theo đúng thứ tự. Suy ra thuật toán đúng và dừng.
Ví dụ: Bài chứng minh, không cần code

-Phát biểu bất biến vòng lặp
Sau bước lặp thứ i (arr[0...n-1], đoạn mảng arr[0..i] chứa $i+1$ phần tử nhỏ nhất của toàn bộ mảng ban đầu, và các phần tử này đã được sắp xếp theo đúng thứ tự tăng dần

-Khởi tạo
Tại vòng lặp thứ i = 0, thuật toán sẽ tìm phần tử nhỏ nhất trong toàn bộ mảng và hoán vị nó với arr[i]

-Duy trì
Giả sử bất biến đúng sau vòng thứ i-1, arr[0..i-1] đã chứa i phần tử nhỏ nhất của mảng và đã được sắp xếp đúng thứ tự. Thuật toán sẽ tìm phần tử nhỏ nhất trong arr[i...n-1], vì đoạn arr[0..i-1] đã chiếm giữ i phần tử nhỏ nhất của toàn bộ mảng, nên phần tử nhỏ nhất trong đoạn còn lại arr[i..n-1] chắc chắn là phần tử nhỏ thứ i+1 của toàn bộ mản và thuật toán sẽ hoán vị phần tử này về vị trí a[i]
=>Phần tử này lớn hơn hoặc bằng tất cả các phần tử trong đoạn arr[0..i-1] việc đặt nó vào vị trí arr[i] giúp đoạn arr[0..i] tiếp tục duy trì thứ tự tăng dần.

-Điều kiện dừng
Khi vòng lặp chạy đến i = n-1 thì chắc chắn vòng lặp sẽ dừng

-Chứng minh thuật toán dừng và đúng
Khi vòng lặp dừng ở bước cuối cùng toàn bộ mảng sẽ chứa (n-1) + 1 = n phần tử nhỏ nhất của mảng theo đúng thứ tự tăng dần. Một mảng kích thước n chứa n phần tử nhỏ nhất được sắp xếp đúng thứ tự chính là mảng đã được sắp xếp hoàn chỉnh.
