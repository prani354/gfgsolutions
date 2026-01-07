from collections import defaultdict
class Solution:
    def countDistinct(self, arr, k):
        # Code here
        res = []
        freq = defaultdict(int)
            
        count = 0
        
        for i,v in enumerate(arr):
            if not freq[v]:
                count += 1
            freq[v] += 1
            
            if i >= k:
                out  = arr[i-k]
                freq[out] -= 1
                
                if not freq[out]:
                    count -= 1
                    
            if i >= k-1:
                res.append(count)
                
        return res
        