# Bài 16. Trọng số trên đỉnh
# Chi phí nằm ở đỉnh thay vì cạnh. Biến đổi bài toán để áp dụng Dijkstra (ví dụ tách mỗi đỉnh
# thành cạnh vào–ra).
# Ví dụ: chi phí đi qua đỉnh v = c[v]

def dijkstra_node_weights(adj, node_costs, start, target):
    peak = len(adj)
    dist = [float('inf')] * peak
    visted = [False] * peak
    dist[start] = node_costs[start]
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
        for v in adj[u]:
            if not visted[v]:
                weight = node_costs[v]     
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight                
    return dist

if __name__ == '__main__':
    from graph_1 import adjacency_list
    adj = {
        0: [1, 2],
        1: [3, 4],
        2: [4],
        3: [5],
        4: [5],
        5: []
    }
    node_costs = [0, 10, 2, 5, 1, 3]  
    start_node = 0
    target_node = 5   
    distance = dijkstra_node_weights(adj, node_costs, start_node, target_node)
    print(f"Khoảng cách ngắn nhất tới đích {target_node} là: {distance[target_node]}")