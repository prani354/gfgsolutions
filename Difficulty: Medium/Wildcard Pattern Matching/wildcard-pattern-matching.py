class Solution:
    def wildCard(self, txt, pat):
        # code here
        
        n, m = len(pat), len(txt)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        
        # Base case
        dp[0][0] = True
    
        
        for i in range(1, n + 1):
            if pat[i - 1] == '*':
                dp[i][0] = dp[i - 1][0]
            else:
                break
    
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if pat[i - 1] == txt[j - 1] or pat[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif pat[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = False
    
        return dp[n][m]