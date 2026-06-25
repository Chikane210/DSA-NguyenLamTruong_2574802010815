def dijkstra(graph, peak, start):
    dist = [float('inf')] * peak
    dist[start] = 0
    visted = [False] * peak
    print('-------------------- Dijkstra -------------------')
    for i in range(peak):
        u = -1
        min_dist = float('inf')
        for j in range(peak):
            if not visted[j] and dist[j] < min_dist:
                min_dist = dist[j]
                u = j       
        if u == -1: break    
        visted[u] = True
        print(f'{i+1}: dinh {u} (dist = {dist[u]})')        
        for v, w in graph[u]:
            if not visted[v]: 
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    print(f'dist[{v}] tam thoi = {dist[v]}')
    return dist


def bellman_ford(graph, peak, start):
    dist = [float('inf')] * peak
    dist[start] = 0
    print('----------------- Bellman-Ford ------------------')
    for i in range(peak - 1):
        print(f'Duyet lan {i + 1}:')
        for u in range(peak):
            if dist[u] == float('inf'): 
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    print(f'dist[{v}] -> {dist[v]} ({u}->{v})')
    return dist


if __name__ == '__main__':
    peak_count = 3
    graph = [
        [(1, 2), (2, 5)], 
        [],                
        [(1, -4)]     
    ]
    dijkstra_res = dijkstra(graph, peak_count, 0)
    print(f'Dijkstra : dist[1] = {dijkstra_res[1]}')
    
    bellman_res = bellman_ford(graph, peak_count, 0)
    print(f'Bellman-Ford: dist[1] = {bellman_res[1]}')