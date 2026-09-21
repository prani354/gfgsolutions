class Solution:
    def longestKSubstr(self, s, k):
        # code here
        
        hashmap = {}
        max_len = -1
        l = 0
        
        for r in range(len(s)):
            
            if s[r] in hashmap:
                hashmap[s[r]] += 1
            else:
                hashmap[s[r]] = 1
            
            while len(hashmap) > k and l <= r:
                hashmap[s[l]] -= 1
                
                if hashmap[s[l]] == 0:
                    del hashmap[s[l]]
                    
                l += 1
                
            
            if len(hashmap) == k:    
                max_len = max(max_len,r-l+1)
            
            
        
            
        return max_len
            
        