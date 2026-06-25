# Bài 15. Dijkstra trên lưới (grid)
# Cho lưới chi phí bên dưới (chi phí khi bước vào mỗi ô). Đi 4 hướng, tìm tổng chi phí nhỏ
# nhất từ ô trên-trái (S) tới ô dưới-phải (đích).
# Lưới chi phí 3×3 (ô tô xanh là điểm xuất phát và đích).
# Ví dụ: lưới 3×3 bên dưới → tổng nhỏ nhất tới đích

import heapq

def dijkstra_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = grid[0][0]
    #luu ba trang thai (tong chi phi, dong, cot)
    min_heap = [(grid[0][0], 0, 0)]
    
    # dinh nghia di chuyen sang (tren, duoi, trai, phai)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1] 
    while min_heap:
        current_cost, r, c = heapq.heappop(min_heap)
        
        #da di den o dich (duoi, phai)
        if r == rows - 1 and c == cols - 1:
            return current_cost          
        if current_cost > dist[r][c]:
            continue
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < rows and 0 <= nc < cols:
                next_cost = current_cost + grid[nr][nc]
                if next_cost < dist[nr][nc]:
                    dist[nr][nc] = next_cost
                    heapq.heappush(min_heap, (next_cost, nr, nc))                  
    return dist[rows-1][cols-1]

if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    
    min_total_cost = dijkstra_grid(grid)
    print(f'tổng chi phí nhỏ nhất từ ô trên-trái (S) tới ô dưới-phải (đích): {min_total_cost}')