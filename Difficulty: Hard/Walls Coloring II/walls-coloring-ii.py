import heapq
from typing import List
class Solution:
    def minCost(self, costs : List[List[int]]) -> int:
        # code here
        if not costs:
            return -1
        
        n = len(costs)
        m = len(costs[0])
        
        if m == 1:
            return costs[0][0] if n == 1 else -1
        
        # dp initially equals first row
        dp = costs[0][:]

        # iterate each house
        for i in range(1, n):
            # find smallest and second smallest in dp
            min1 = min2 = float('inf')
            idx1 = idx2 = -1

            for j in range(m):
                if dp[j] < min1:
                    min2, idx2 = min1, idx1
                    min1, idx1 = dp[j], j
                elif dp[j] < min2:
                    min2, idx2 = dp[j], j

            # new dp row
            new_dp = [0] * m

            for j in range(m):
                # if same color as min1, use second min
                if j == idx1:
                    new_dp[j] = costs[i][j] + min2
                else:
                    new_dp[j] = costs[i][j] + min1

            dp = new_dp

        return min(dp)
                    
                
        
        
            