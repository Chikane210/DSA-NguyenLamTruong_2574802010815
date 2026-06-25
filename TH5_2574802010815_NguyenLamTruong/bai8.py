# Bài 8. Số đỉnh trong bán kính D
# Trên G1, đếm số đỉnh có khoảng cách ngắn nhất từ nguồn 0 thỏa ≤ D.
# Ví dụ: D = 3 → 3 đỉnh (0, 2, 1)
from graph_1 import adjacency_list

def dijstra_distance(adj, s):
    peak = len(adj)
    dist = [float('inf')] * peak
    dist[s] = 0
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

def countNode_shortestThan_D(dist, D):
    count = 0 
    node = []
    for i in range(len(dist)):
        if dist[i] <= D:
            node.append(i) 
            count += 1
    return count, node

if __name__ == '__main__':   
    adj = adjacency_list()
    start = 0
    while True:
        try: 
            D = int(input('D: '))
            if D >= 0:
                break
            print('D >= 0')
        except ValueError:
            print('nhap so nguyen')
    dist = dijstra_distance(adj, start)
    count, node = countNode_shortestThan_D(dist, D)   
    print(f'D = {D} -> {count} dinh ({node})')