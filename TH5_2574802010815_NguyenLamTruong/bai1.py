# Bài 1. Biểu diễn đồ thị có trọng số
# Cho đồ thị có hướng bên dưới (trọng số dương). Hãy xây dựng danh sách kề (adjacency
# list). Đây là bước chuẩn bị cho mọi bài Dijkstra phía sau — các bài 1–8 đều dùng chung đồ thị
# này.

def adjacency_list():
    adj ={0:[(1,4), (2,1)],
          1:[(3,1)],
          2:[(1,2), (3,5), (4,8)],
          3:[(4,3), (5,6)],
          4:[(5,2)],
          5:[]    
        }
    return adj

adj = adjacency_list()
for i in range(len(adj)):
    print(f'{i}: {adj[i]}')