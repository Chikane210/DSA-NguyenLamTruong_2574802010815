# Bài 5. Đồ thị vô hướng có trọng số
# Áp dụng Dijkstra cho đồ thị vô hướng các thành phố bên dưới. Tìm khoảng cách ngắn nhất
# từ thành phố A tới các thành phố còn lại.

def graph():
    adj = {
        'A': [('B', 5), ('C', 3)],
        'B': [('A', 5), ('C', 1), ('D', 2)],
        'C': [('A', 3), ('B', 1), ('D', 6)],
        'D': [('B', 2), ('C', 6), ('E', 4)],
        'E': [('D', 4)]  
    }
    return adj

def dijkstra(adj, s):
    dist = {peak: float('inf') for peak in adj}
    dist[s] = 0
    visited = {peak: False for peak in adj}
    for i in range(len(adj)):
        u = -1
        min_dist = float('inf')
        for node in adj:
            if not visited[node] and dist[node] < min_dist:
                min_dist = dist[node]
                u = node       
        if u == -1:
            break 
        visited[u] = True
        for v, w in adj[u]:
            if not visited[v]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w     
    return dist

if __name__ == '__main__':
    adj = graph()
    distance = dijkstra(adj, 'A')
    for k, v in distance.items():
        print(f'{k}={v}', end=' ')