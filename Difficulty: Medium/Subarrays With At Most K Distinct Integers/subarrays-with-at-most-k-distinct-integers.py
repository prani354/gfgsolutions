from collections import defaultdict
class Solution:
    def countAtMostK(self, arr, k):
        # Code here
        count = 0
        hash_map = defaultdict(int)
        l = 0
        
        for r in range(len(arr)):
            
            hash_map[arr[r]] += 1
            
            if hash_map[arr[r]] == 1:
                k -= 1
                
            while k < 0:
                hash_map[arr[l]] -= 1
                
                if hash_map[arr[l]] == 0:
                    k += 1
                    
                l += 1
                
            count += (r - l + 1)
            
        return count