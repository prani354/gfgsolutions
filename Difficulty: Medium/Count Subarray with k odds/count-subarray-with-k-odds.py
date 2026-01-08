class Solution:
    def countSubarrays(self, arr, k):
        # Code here
        hash_map = {0:1}
        count = 0
        odd = 0
        n = len(arr)
        
        for i in range(n):
            if arr[i] % 2 != 0:
                odd += 1
                
            if odd - k in hash_map:
               count += hash_map[odd-k]
               
            hash_map[odd] = hash_map.get(odd,0) + 1
            
        return count