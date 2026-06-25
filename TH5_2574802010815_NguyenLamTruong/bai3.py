# Bài 3. Dijkstra cơ bản: nguồn tới mọi đỉnh
# Cài đặt Dijkstra (bản O(V²)) tìm khoảng cách ngắn nhất từ nguồn s = 0 tới tất cả các đỉnh
# của G1.
# Ví dụ: s = 0 → dist = [0, 3, 1, 4, 7, 9]

from graph_1 import adjacency_list

def dijkstra(adj,s):
    peak = len(adj)
    dist = [float('inf')] * peak #khoi tao mang khoang cach (gtr mac dinh = inf)
    dist[s] = 0
    visted = [False] * peak
    
    for i in range(peak):
        #tim dinh u chx dc duyet
        u = -1
        min_dist = float('inf')
        for j in range(peak):
            if not visted[j] and dist[j] < min_dist:
                min_dist = dist[j]
                u = j
        if u == -1:
            break #ko tim duoc dinh co the di toi tiep theo
        visted[u] = True #danh dau dinh u da dc xu ly
        for v, w in adj[u]:
            if not visted[v]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    return dist
if __name__ == '__main__':
    s = 0
    adj = adjacency_list()
    distance = dijkstra(adj,s)
    print(f's = {0} -> {distance}')
    
