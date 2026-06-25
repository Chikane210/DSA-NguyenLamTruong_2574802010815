# Bài 11. Nhiều nguồn (multi-source)
# Cho một tập đỉnh nguồn. Tìm với mỗi đỉnh khoảng cách tới nguồn gần nhất. Gợi ý: thêm
# một "siêu nguồn" nối tới mọi nguồn với trọng số 0.
# Ví dụ: nguồn = {0, 3} → dist[i] = min tới 0 hoặc 3

import heapq
from graph_1 import adjacency_list

def dijkstra_multi_source(adj, sources):
    dist = {node: float('inf') for node in adj}
    min_heap = []
    for src in sources:
        if src in dist:
            dist[src] = 0
            heapq.heappush(min_heap, (0, src))
    while min_heap:
        current_dist, u = heapq.heappop(min_heap)
        if current_dist > dist[u]:
            continue         
        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(min_heap, (dist[v], v))               
    return dist

if __name__ == '__main__':
    adj = adjacency_list()
    sources = [int(x) for x in input('start/end: ').split()]         
    shortest_distances = dijkstra_multi_source(adj, sources)
    for node, distance in shortest_distances.items():
        print(f'{node}: {distance}')