# Bài 7. Truy vết đường đi (reconstruct path)
# Dùng mảng parent[] để truy ngược và in ra dãy đỉnh trên đường đi ngắn nhất từ 0 tới 4 của
# G1 (đường tô xanh bên dưới)

from graph_1 import adjacency_list

def reconstruct_path(start, end, parent):
    path = []
    current = end
    while current != -1: 
        path.append(current)
        if current == start:
            break
        current = parent[current]
    path.reverse()
    if path[0] == start:
        return path
    else:
        return None
    
def dijstra_distance(adj, start):
    peak = len(adj)
    parent = [-1] * peak
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
                    parent[v] = u
    return parent

if __name__ == '__main__':   
    adj = adjacency_list()
    start = 0
    parent = dijstra_distance(adj, start)
    end = 4
    result = reconstruct_path(start, end, parent)
    print(result)