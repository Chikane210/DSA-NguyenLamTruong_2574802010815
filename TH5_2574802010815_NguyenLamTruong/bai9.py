# Bài 9. Dijkstra với hàng đợi ưu tiên
# Cài đặt Dijkstra dùng priority queue / min-heap, đạt độ phức tạp O((V + E) log V). So sánh
# tốc độ với bản O(V²) trên đồ thị thưa.
# Ví dụ: n=10^5, m=2·10^5 → cần bản heap
# Ràng buộc: 1 ≤ n,m ≤ 2·10^5
import heapq
import time
import random

def dijkstra_heap(adj, start):
    dist = {node: float('inf') for node in adj}
    dist[start] = 0
    min_heap = [(0, start)]
    while min_heap:
        current_dist, u = heapq.heappop(min_heap)
        if current_dist > dist[u]:
            continue
        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(min_heap, (dist[v], v))            
    return dist

def dijstra_distance(adj, start):
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

def create_graph(v_count, e_count):
    adj = {i: [] for i in range(v_count)}
    for _ in range(e_count):
        u = random.randint(0, v_count - 1)
        v = random.randint(0, v_count - 1)
        w = random.randint(1, 20)
        if u != v:
            adj[u].append((v, w))
    return adj

if __name__ == '__main__':
    while True:
        try:
            V = int(input('V: '))
            E = int(input('E: '))
            if V >= 0 and E >= 0:
                break
            print('Cac gia tri dien vao >= 0')
        except ValueError:
            print('nhap so nguyen')
    graph = create_graph(V, E)

    startTime = time.time()
    dijkstra = dijstra_distance(graph, 0)
    endTime = time.time()
    print(f'Dijkstra O(V^2): {endTime - startTime:.5f}')
    
    startTime_1 = time.time()
    dijkstraHeap = dijkstra_heap(graph, 0)
    endTime_1 = time.time()
    print(f'Dijkstra Heap: {endTime_1 - startTime_1:.5f}')