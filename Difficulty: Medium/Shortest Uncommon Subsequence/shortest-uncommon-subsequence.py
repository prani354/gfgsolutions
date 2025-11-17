#User function Template for python3

class Solution:
    def shortestUnSub(self, S, T):
        # code here 
        n, m = len(S), len(T)
        INF = 10**9
    
        # Precompute next occurrence of each char in T
        next_pos = [[-1] * 26 for _ in range(m + 1)]
        
        for c in range(26):
            next_pos[m][c] = -1  # beyond last index, nothing exists
    
        for i in range(m - 1, -1, -1):
            for c in range(26):
                next_pos[i][c] = next_pos[i + 1][c]
            next_pos[i][ord(T[i]) - ord('a')] = i
    
        # DP table
        dp = [[INF] * (m + 1) for _ in range(n + 1)]
    
        # If S is empty, no subsequence possible
        for j in range(m + 1):
            dp[n][j] = INF
    
        # If T is empty, any char in S forms an uncommon subsequence of length 1
        for i in range(n):
            dp[i][m] = 1
    
        # Fill dp bottom-up
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
    
                # Option 1: skip S[i]
                skip = dp[i + 1][j]
    
                # Option 2: take S[i]
                ch = ord(S[i]) - ord('a')
                k = next_pos[j][ch]
    
                if k == -1:
                    take = 1   # S[i] does not occur in T[j:], so it's unique
                else:
                    take = 1 + dp[i + 1][k + 1]
    
                dp[i][j] = min(skip, take)
    
        ans = dp[0][0]
        return -1 if ans >= INF else ans