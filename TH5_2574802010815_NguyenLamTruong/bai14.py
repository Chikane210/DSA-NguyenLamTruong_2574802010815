# Bài 14. Đường đi ngắn nhì
# Tìm độ dài đường đi ngắn nhì (second shortest, có thể dùng lại cạnh) từ s tới t. Gợi ý: lưu
# hai khoảng cách tốt nhất cho mỗi đỉnh.
# Ví dụ: ngắn nhất = 7, ngắn nhì = 9

def dijkstra_second_shortest(adj, start):
    peak = len(adj)
    bestShortest_dist = [float('inf')] * peak  # Ngắn nhất
    secondShortest_dist = [float('inf')] * peak  # Ngắn nhì
    bestShortest_dist[start] = 0

    for i in range(2 * peak):
        for u in range(peak):
            if bestShortest_dist[u] != float('inf'):
                for v, w in adj[u]:
                    d = bestShortest_dist[u] + w
                    if d < bestShortest_dist[v]:
                        secondShortest_dist[v] = bestShortest_dist[v]
                        bestShortest_dist[v] = d
                    elif bestShortest_dist[v] < d and d < secondShortest_dist[v]:
                        secondShortest_dist[v] = d

            if secondShortest_dist[u] != float('inf'):
                for v, w in adj[u]:
                    d = secondShortest_dist[u] + w
                    if bestShortest_dist[v] < d and d < secondShortest_dist[v]:
                        secondShortest_dist[v] = d
                        
    return bestShortest_dist, secondShortest_dist

if __name__ == '__main__':
    from graph_1 import adjacency_list
    adj = adjacency_list()
    s = 0
    while True:
        try:
            t = int(input('t: '))
            if t >= 0 and t <= len(adj)-1:
                break
            elif t < 0:
                print('t phai >= 0')
            elif t > len(adj)-1:
                print(f'dinh phai be hon {len(adj)}')
        except ValueError:
            print('nhap so nguyen')
    bestShortest_dist, secondShortest_dist = dijkstra_second_shortest(adj, s)
    print(f'ngắn nhất: {bestShortest_dist[t]}')
    print(f'ngắn nhì : {secondShortest_dist[t]}')