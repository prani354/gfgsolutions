from functools import lru_cache
class Solution: 
    def chocolatePickup(self, mat): 
        # code here
        n = len(mat)

        @lru_cache(None)
        def dfs(r1, c1, r2):
            c2 = r1 + c1 - r2
            # Out of bounds or blocked
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n or mat[r1][c1] == -1 or mat[r2][c2] == -1:
                return float('-inf')
            
            # Reached bottom-right corner
            if r1 == n - 1 and c1 == n - 1:
                return mat[r1][c1]
    
            # Collect chocolates
            res = mat[r1][c1]
            if (r1, c1) != (r2, c2):
                res += mat[r2][c2]
    
            # Move combinations (both move one step)
            res += max(
                dfs(r1 + 1, c1, r2 + 1),  # down, down
                dfs(r1, c1 + 1, r2),      # right, down
                dfs(r1 + 1, c1, r2),      # down, right
                dfs(r1, c1 + 1, r2 + 1)   # right, right
            )
    
            return res
    
        ans = dfs(0, 0, 0)
        return max(0, ans)
            