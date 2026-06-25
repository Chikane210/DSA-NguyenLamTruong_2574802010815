# Bài 6. Đường đi ngắn nhất giữa hai đỉnh
# Trên G1, tìm độ dài đường đi ngắn nhất từ s = 0 tới t = 4. Có thể dừng sớm khi lấy được t ra
# khỏi hàng đợi.
# Ví dụ: s = 0, t = 4 → 7
from graph_1 import adjacency_list

def dijkstra_early_stop(adj, s, t):
    peak = len(adj)
    dist = [float('inf')] * peak
    dist[s] = 0
    visited = [False] * peak
    for i in range(peak):
        u = -1
        min_dist = float('inf')
        for j in range(peak):
            if not visited[j] and dist[j] < min_dist:
                min_dist = dist[j]
                u = j      
        if u == -1:
            break 
        visited[u] = True
        if u == t:
            break
        for v, w in adj[u]:
            if not visited[v]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    return dist[t]

if __name__ == '__main__':
    adj = adjacency_list()   
    s = 0
    t = 4
    shortest = dijkstra_early_stop(adj, s, t)
    if shortest == float('inf'):
        print(f"s = {s}, t = {t} -> -1")
    else:
        print(f"s = {s}, t = {t} -> {shortest}")