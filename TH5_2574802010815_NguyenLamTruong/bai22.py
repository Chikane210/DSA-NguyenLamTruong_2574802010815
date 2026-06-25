# Bài 22. Giới hạn số cạnh trung chuyển
# Tìm đường đi rẻ nhất từ s tới t dùng tối đa k cạnh (k điểm dừng). Gợi ý: Dijkstra/BFS phân
# lớp theo số cạnh, trạng thái (đỉnh, số_cạnh_đã_dùng).
# Ví dụ: k=1 điểm dừng → đường rẻ nhất ≤ 2 cạnh
def dijkstra_k_stops(adj, start, target, k_stops):
    peak = len(adj)
    max_edges = k_stops + 1
    dist = [[float('inf')] * (max_edges + 1) for _ in range(peak)]
    dist[start][0] = 0
    queue = [(0, start, 0)]
    while queue:
        min_idx = 0
        for i in range(1, len(queue)):
            if queue[i][0] < queue[min_idx][0]:
                min_idx = i
        current_cost, u, edges_used = queue.pop(min_idx)
        if current_cost > dist[u][edges_used]:
            continue
        if u == target:
            return current_cost
        if edges_used < max_edges:
            for v, w in adj[u]:
                next_edges = edges_used + 1
                if current_cost + w < dist[v][next_edges]:
                    dist[v][next_edges] = current_cost + w
                    queue.append((current_cost + w, v, next_edges))
    min_res = min(dist[target])
    if min_res != float('inf'):
        return min_res
    else: 
        return -1
if __name__ == '__main__':
    from graph_1 import adjacency_list
    adj = adjacency_list()   
    s = 0
    t = 3
    k = 1 
    ans = dijkstra_k_stops(adj, s, t, k)
    if ans != -1:
        print(f'Chi phí rẻ nhất từ {s} đến {t} là: {ans}')
    else:
        print(f'Không có đường đi nào thỏa mãn dưới {k} điểm dừng!')