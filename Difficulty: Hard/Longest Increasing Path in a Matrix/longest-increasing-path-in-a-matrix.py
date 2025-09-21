#User function Template for python3

class Solution:
    def longIncPath(self, matrix, n, m):
        # Code here
        dp = {}  #dfs
        
        def dfs(i,j,prev):
            if 0 <= i < n and 0 <= j < m and prev < matrix[i][j]:
                if (i,j) not in dp:
                    dp[(i,j)] = 1 + max(dfs(i+1,j,mat[i][j]),dfs(i,j+1,mat[i][j]),dfs(i-1,j,mat[i][j]),dfs(i,j-1,mat[i][j]))
                
                return dp[(i,j)]
            return 0
            
        for i in range(n):
            for j in range(m):
                if (i,j) not in dp:
                    dfs(i,j,-1)
                    
        return max(dp.values())