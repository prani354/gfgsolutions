class Solution:
    def minCutCost(self, n, cuts):
        # code here
        
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)
        
        dp = [[0] * m for _ in range(m)]
        
        for l in range(2,m):
            
            for i in range(m-l):
                j = i + l  #end of cut
                
                dp[i][j] = float('inf')
                
                for k in range(i+1,j):  #every possible cut
                
                    cost = cuts[j] - cuts[i] + dp[i][k] + dp[k][j]
                    dp[i][j] = min(dp[i][j],cost)
                    
        return dp[0][m-1]
        
        