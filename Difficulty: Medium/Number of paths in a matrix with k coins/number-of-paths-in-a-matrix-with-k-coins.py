class Solution:
    def numberOfPath(self, mat, k):
        # code here
        n, m = len(mat), len(mat[0])
        memo = {}
    
        def dfs(i, j, coins_left):
            # Out of bounds
            if i >= n or j >= m:
                return 0
            
            # Base case: bottom-right cell
            if i == n - 1 and j == m - 1:
                return 1 if coins_left == mat[i][j] else 0
            
            # Memoization check
            if (i, j, coins_left) in memo:
                return memo[(i, j, coins_left)]
            
            # Move down and right
            remaining = coins_left - mat[i][j]
            if remaining < 0:
                return 0  # No need to continue if sum exceeds k
            
            down = dfs(i + 1, j, remaining)
            right = dfs(i, j + 1, remaining)
            
            memo[(i, j, coins_left)] = down + right
            return memo[(i, j, coins_left)]
    
        return dfs(0, 0, k)
    
