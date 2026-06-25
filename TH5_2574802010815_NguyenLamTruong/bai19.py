# Bài 19. Đường đi xác suất lớn nhất
# Mỗi cạnh có xác suất "thành công" trong [0,1]. Tìm đường đi từ s tới t có tích xác suất lớn
# nhất. Gợi ý: dùng -log để đưa về bài cộng trọng số, hoặc đổi phép relax sang nhân/lấy max.
# Ví dụ: maximize product of probabilities

import math

def dijkstra(adj, start):
    peak = len(adj)
    dist = [float('inf')] * peak
    dist[start] = 0
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

def max_probability(adj_list, start, target):
    log_adj = [[] for _ in range(len(adj_list))]
    for u in range(len(adj_list)):
        for v, w in adj_list[u]:
            log_w = -math.log(w) if w > 0 else float('inf')
            log_adj[u].append((v, log_w))
    min_dist = dijkstra(log_adj, start)
    if min_dist[target] == float('inf'):
        return 0
    return math.exp(-min_dist[target])

if __name__ == '__main__':
    from graph_1 import adjacency_list 
    adj = adjacency_list()
    s = 0
    t = 1
    prob = max_probability(adj, s, t)
    print(f'Xác suất thành công cao nhất đạt được: {prob * 100}%')