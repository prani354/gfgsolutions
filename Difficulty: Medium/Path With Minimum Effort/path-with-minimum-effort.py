from collections import deque
class Solution:
    def minCostPath(self, mat):
        # code here 
        if not mat or not mat[0]:
            return 0
            
        n, m = len(mat), len(mat[0])
        
        # Min-heap: (max_effort_so_far, row, col)
        heap = [(0, 0, 0)]
        
        # Track minimum effort to reach each cell
        efforts = [[float('inf')] * m for _ in range(n)]
        efforts[0][0] = 0
        
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while heap:
            current_effort, x, y = heapq.heappop(heap)
            
            # If we reached destination, return the effort
            if x == n - 1 and y == m - 1:
                return current_effort
            
            # If we found a better path to this cell already, skip
            if current_effort > efforts[x][y]:
                continue
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < m:
                    # Calculate effort for this move
                    new_effort = max(current_effort, abs(mat[nx][ny] - mat[x][y]))
                    
                    if new_effort < efforts[nx][ny]:
                        efforts[nx][ny] = new_effort
                        heapq.heappush(heap, (new_effort, nx, ny))
        
        return efforts[n-1][m-1]
