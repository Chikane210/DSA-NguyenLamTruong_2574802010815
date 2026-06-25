# Bài 2. Tính tay đường đi ngắn nhất
# Với đồ thị G1 ở Bài 1, chạy tay thuật toán Dijkstra từ nguồn s = 0. Lập bảng ghi lại dist[]
# sau mỗi vòng chọn đỉnh và thứ tự các đỉnh được "chốt".
# Ví dụ: thứ tự chốt: 0, 2, 1, 3, 4, 5

Xuất phát từ nguồn s = 0
Đặt T = {0,1,2,3,4,5}
L(0) = 0, L(1)=L(2)=L(3)=L(4)=L5= inf
P(0)=P(1)=P(2)=P(3)=P(4)=P(5)=null

L(0) = min{L(x)} = 0, visted = 0 & T - {0} = {1,2,3,4,5}
visted != 5
-Xét đỉnh 1 & 2 kề với 0
L(1) = inf > L(0) + w(0,1) = 0 + 4 = 4 =>L(1) = 4. P(1) = 0
L(2) = inf > L(0) + w(0,2) = 0 + 1= 1 =>L(2) = 1. P(2) = 0

L(2) = min{L(x)} = 1, visted = 2 & T - {2} = {1,3,4,5}
visted != 5
-Xet dinh 1, 3, 4 ke voi 2
L(1) = 4 > L(2) + w(2,1) = 1 + 2 = 3 =>L(1) = 3.P(1) = 2
L(3) = inf > L(2) + w(2,3) = 1 + 5 = 6=>L(3) = 6.P(3) = 2
L(4) = inf > L(2) + w(2,4) = 1 + 8 = 9=>L(4) = 9.P(4) = 2

L(1) = min{L(x)} = 3, visted = 1 & T - {1} = {3,4,5}
visted != 5
-Xet dinh 3 ke voi 1
L(3) = 6 > L(1) + w(1,3) = 3 + 1 = 4=>L(3) = 4.P(3) = 1

L(3) = min{L(x)} = 4, visted = 3 & T - {3} = {4,5}
visted != 5
-Xet dinh 4 & 5 ke voi 3
L(4) = 9 > L(3) + w(3,4) = 4 + 3 = 7=>L(4) = 7.P(4) = 3
L(5) = inf > L(3) + w(3,5) = 4 + 6 = 10=>L(5) = 10.P(5) = 3

L(4) = min{L(x)} = 7, visted = 4 & T - {4} = {5}
visted != 5
-Xet dinh 5 ke voi 4
L(5) = 10 > L(4) + w(4,5) = 7 + 2 = 9=>L(5) = 9.P(5) = 4

L(5) = min{L(x)} = 9, visted = 5 & T - {5} = null
visted == 5. Ket thuc
L(5) = 9 la do dai duong di ngan nhat tu 0->5
=>Duong di ngan nhat/Thu tu dinh duoc 'chot': 0 -> 2 -> 1 -> 3 -> 4 -> 5

# Bài 10. Chọn cài đặt theo mật độ đồ thị
# Cho biết khi nào nên dùng bản O(V²) (đồ thị dày) và khi nào dùng heap O((V + E) log V) (đồ thị thưa). Chứng
# minh bằng phân tích độ phức tạp theo V và E.
# Ví dụ: E ≈ V² → O(V²) tốt; E ≈ V → heap tốt

-Truong hop E ≈ V:
(V+V).logV = 2.V.logV -> O(V.logV)
Vi VlogV < V^2 => Ban Dijkstra Heap toi uu hon

-Truong hop E ≈ V²
(V+V²).logV = VlogV + V²logV -> O(V²logV)
Vi V²logV > V² => Ban Dijkstra thuong toi uu hon


