class Solution:
    def mergeStones(self, stones, k):
        # code here
        n = len(stones)
    
        # Check if merging to single pile is possible
        if (n - 1) % (k - 1) != 0:
            return -1
        
        # Prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]
    
        # dp[i][j] = min cost to merge stones[i..j]
        dp = [[0] * n for _ in range(n)]
        
        # interval length
        for length in range(k, n + 1):  # at least k needed to merge
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float("inf")
                
                # split only at step of k-1
                for m in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j])
                
                # if this segment can form 1 pile, add merge cost
                if (length - 1) % (k - 1) == 0:
                    dp[i][j] += prefix[j + 1] - prefix[i]
        
        return dp[0][n - 1]
            
            
