class Solution:
    def findWays(self, n):
        # code here
        
        if n % 2 != 0:
            return 0
            
        pairs = n // 2
        
        dp = [0] * (pairs + 1)
        dp[0] = 1
        
        for i in range(1, pairs + 1):
            
            total = 0
        
            for j in range(i):
            
                total += dp[j] * dp[i - 1 - j]
            dp[i] = total
    
        return dp[pairs]
        