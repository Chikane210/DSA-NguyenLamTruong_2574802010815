# Bài 20. K đường đi ngắn nhất
# Tìm độ dài của K đường đi ngắn nhất (cho phép lặp đỉnh) từ s tới t. Gợi ý: Dijkstra mở rộng
# cho phép một đỉnh được lấy ra tối đa K lần.
# Ví dụ: K=3 → [7, 9, 10]

def dijkstra_k_shortest(adj, start, target, k):
    peak = len(adj)

    dist = [[] for i in range(peak)]
    count = [0] * peak
    queue = [(0, start)]
    while queue:
        min_idx = 0
        for i in range(1, len(queue)):
            if queue[i][0] < queue[min_idx][0]:
                min_idx = i
        current_dist, u = queue.pop(min_idx)
        if count[u] >= k:
            continue
        dist[u].append(current_dist)
        count[u] += 1
        if u == target and count[target] == k:
            break
        for v, w in adj[u]:
            if count[v] < k:
                next_dist = current_dist + w
                queue.append((next_dist, v))     
    return dist[target]

if __name__ == '__main__':
    from graph_1 import adjacency_list
    adj = adjacency_list()
    s = 0
    t = 4
    K = 3   
    k_paths = dijkstra_k_shortest(adj, s, t, K)
    print(f"Kết quả danh sách độ dài: {k_paths}")