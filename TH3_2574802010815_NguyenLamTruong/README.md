Bài 25. Chứng minh tính đúng đắn (loop invariant)
Phát biểu và chứng minh bất biến vòng lặp của bubble sort: sau lượt thứ i, i phần tử lớn
nhất đã nằm đúng vị trí ở cuối mảng. Dùng nó để chứng minh thuật toán dừng và đúng.
Ví dụ: Bài chứng minh, không cần code

-Vòng lặp ngoài (lượt thực hiện)
Sau lần lặp thứ i có phân tử ở vị tri n-i+1 đến n đã được sắp xếp đúng thứ tự và không thay đổi nữa

-Vòng lặp trong (So sánh các phần tử)
Mỗi lượt duyệt thuật toán sẽ so sánh phần tử kế tiếp nhau và hoán đổi chúng nếu sai thứ tự (bé -> lớn / lớn-> bé)

-Điều kiện dừng
Vòng lặp sẽ dừng lại nếu phát hiện các phần từ đều đã nằm đúng thứ tự (không có phép hoán đổi nào xảy ra)

-Chứng minh thuật toán dừng và đúng
Sau mỗi lượt lặp phần tử lớn/nhỏ nhất trong khoảng arr[0...n-i-1] luôn được đẩy về cuối mảng. Do đó nên lúc nào phần tử arr[n-i+1....n] luôn được sắp xếp đúng vị trí và thuật toán sẽ dừng khi duyệt hết lượt n-1 hoặc phát hiện không có phép hoán đổi nào xảy ra