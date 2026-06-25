# Bài 21. Dijkstra trên trạng thái mở rộng
# Trạng thái = (đỉnh, thông tin phụ) — ví dụ lượng nhiên liệu còn lại, hoặc số vé miễn phí. Tìm
# chi phí nhỏ nhất tới đích trên đồ thị trạng thái mở rộng.
# Ví dụ: state = (đỉnh, nhiên_liệu)

def dijkstra_extended_state(adj, node_prices, start, target, max_fuel):
    peak = len(adj)
    dist = [[float('inf')] * (max_fuel + 1) for i in range(peak)]
    dist[start][0] = 0
    queue = [(0, start, 0)]
    visted = [[False] * (max_fuel + 1) for _ in range(peak)]
    while queue:
        min_idx = 0
        for i in range(1, len(queue)):
            if queue[i][0] < queue[min_idx][0]:
                min_idx = i
        current_cost, u, fuel = queue.pop(min_idx)  
        if visted[u][fuel]:
            continue
        visted[u][fuel] = True
        if u == target:
            return current_cost
        if fuel < max_fuel:
            next_cost = current_cost + node_prices[u]
            if next_cost < dist[u][fuel + 1]:
                dist[u][fuel + 1] = next_cost
                queue.append((next_cost, u, fuel + 1))
        for v, fuel_cost in adj[u]:
            if fuel >= fuel_cost:
                remain_fuel = fuel - fuel_cost
                if current_cost < dist[v][remain_fuel]:
                    dist[v][remain_fuel] = current_cost
                    queue.append((current_cost, v, remain_fuel))              
    return float('inf')
if __name__ == '__main__':
    from graph_1 import adjacency_list
    adj = adjacency_list()
    node_prices = [10, 5, 2, 9]
    start_node = 0
    target_node = 3
    capacity = 3
    min_money = dijkstra_extended_state(adj, node_prices, start_node, target_node, capacity)
    print(f'Chi phi nho nhat de den dich: {min_money}')