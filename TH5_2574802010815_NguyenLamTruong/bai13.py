# Bài 13. Đếm số đường đi ngắn nhất
# Đếm số lượng đường đi ngắn nhất khác nhau từ nguồn tới mỗi đỉnh (cùng độ dài tối thiểu).
# Ví dụ: có 2 đường cùng dài 7 tới đỉnh t → 2

def dijkstra_count_paths(adj, start):
    peak = len(adj)
    dist = [float('inf')] * peak
    visted = [False] * peak
    ways = [0] * peak
    
    dist[start] = 0
    ways[start] = 1 
    
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
                    ways[v] = ways[u]
                elif dist[u] + w == dist[v]:
                    ways[v] += ways[u]         
    return dist, ways

if __name__ == '__main__':
    from graph_1 import adjacency_list
    adj = adjacency_list()    
    start = 0
    distances, count = dijkstra_count_paths(adj, start)
    for i in range(len(adj)):
        print(f'có {count[i]} đường cùng dài {distances[i]} tới đỉnh t → {i}')