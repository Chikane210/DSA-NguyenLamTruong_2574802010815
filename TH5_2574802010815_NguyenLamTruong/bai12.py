# Bài 12. Đi qua đỉnh bắt buộc
# Tìm đường đi ngắn nhất từ s tới t bắt buộc đi qua đỉnh k. Gợi ý: dist(s,k) + dist(k,t).
# Ví dụ: s=0, t=5, qua k=2

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

def shortest_path(adj, s, t, k):
    dist_s= dijstra_distance(adj, s)
    dist_k = dijstra_distance(adj, k)
    if dist_s[k] == float('inf') or dist_k[t] == float('inf'):
        return float('inf')
    return dist_s[k] + dist_k[t]

if __name__ == '__main__':
    from graph_1 import adjacency_list
    adj = adjacency_list()  
    s = 0
    while True:
        try:
            t = int(input('t: '))
            k = int(input('k: '))
            if (t >=0 and k>=0) and (t < len(adj) and k < len(adj)):
                break
            if t >= len(adj) or k >= len(adj):
                print('vuot qua kich thuoc cho phep')
            if t < 0 and k < 0:
                print('t va k phai >= 0')
        except ValueError:
            print('nhap so nguyen')
    total_distance = shortest_path(adj, s, t, k)
    print(f"Đường đi ngắn nhất từ {s} đến {t} bắt buộc đi qua đỉnh {k}:")
    if total_distance != float('inf'):
        print(f'Tong khoang cach: {total_distance}')
    else:
        print('Ko phat hien duong di hop le')