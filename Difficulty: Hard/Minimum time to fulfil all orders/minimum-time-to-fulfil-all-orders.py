class Solution:
    def minTime(self, ranks, n):
        # code here
        ranks.sort()
        
        low = 0
        high = max(ranks) * (n * (n+1) // 2)
        
        def donut_in_time(t):
            res = 0
            
            for r in ranks:
                
                if t < r:
                    break
                
                val = (2 * t) // r
                k = int((math.sqrt(1 + 4 * val) - 1) / 2)  #qudratic solution
                 
                res += k
                
                if res >= n:
                    return res
            return res
            
        while low < high:
            
            mid = (low + high) // 2
            
            if donut_in_time(mid) >= n:
                high = mid
                
            else:
                low = mid + 1
                
        return low
        
        