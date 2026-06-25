# Bài 4. In khoảng cách tới mọi đỉnh
# Sau khi chạy Dijkstra, in dist[i] cho mọi đỉnh; in -1 (hoặc ∞) nếu đỉnh không tới được từ
# nguồn.
# Ví dụ: dist[5] = 9 ; đỉnh không nối → -1
from graph_1 import adjacency_list

def dijstra_distance(adj, s):
    peak = len(adj)
    dist = [float('inf')] * peak
    dist[s] = 0
    visted = [False] * peak
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
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    return dist

def print_dijstra_distance(n,dist):
    for i in range(n):
        if dist[i] == float('inf'):
            print(f'dist[{i}] = -1')
        else:
            print(f'dist[{i}] = {dist[i]}')
            
if __name__ =='__main__':
    adj = adjacency_list()
    n = len(adj)
    distance = dijstra_distance(adj,0)
    print_dijstra_distance(n=n, dist=distance)     
    
    