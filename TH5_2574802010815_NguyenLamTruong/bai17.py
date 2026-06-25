# Bài 17. Đường đi bottleneck (minimax)
# Tìm đường đi từ s tới t sao cho cạnh lớn nhất trên đường là nhỏ nhất (minimax /
# widest-path biến thể). Sửa phép "relax" của Dijkstra cho phù hợp.
# Ví dụ: minimize max edge weight on path

def dijkstra_bottleneck(adj, start):
    peak = len(adj)
    dist = [float('inf')] * peak
    visted = [False] * peak
    dist[start] = 0
    
    for i in range(peak):
        u = -1
        min_dist = float('inf')
        for j in range(peak):
            if not visted[j] and dist[j] < min_dist:
                min_dist = dist[j]
                u = j       
        if u == -1:
            break   
        visted[u] = True
        for v, w in adj[u]:
            if not visted[v]:
                new_bottleneck = max(dist[u], w)
                if new_bottleneck < dist[v]:
                    dist[v] = new_bottleneck         
    return dist

if __name__ == '__main__':
    from graph_1 import adjacency_list
    adj = adjacency_list()   
    s = 0
    while True:
        t = int(input('Nhap dinh t (0-5): '))
        if 0 <= t < len(adj):
            break
        print('Dinh khong hop le. Vui long nhap lai.')
    dist = dijkstra_bottleneck(adj, s)
    if dist[t] != float('inf'):
        print(f'Duong di ngan nhat tu {s} den {t}: {dist[t]}')
    else:
        print('Duong di khong ton tai')