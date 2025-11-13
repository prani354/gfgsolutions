class Solution:
    def isInterleave(self, s1, s2, s3):
        # code here
        if len(s1) + len(s2) != len(s3):
            return False
    
        n1, n2 = len(s1), len(s2)
        
        # DP table creation
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        
        # Base case
        dp[0][0] = True
        
            
        # First row: only s2
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        
        # First column: only s1
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        
        # Fill the rest of dp table
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                take_from_s1 = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                take_from_s2 = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                dp[i][j] = take_from_s1 or take_from_s2
        
        return dp[n1][n2]
               