class Solution:
    def longestSubstr(self, s, k):
        # Code here
        left = 0
        res = 0
        freq = {}
        max_freq = 0
        
        for right in range(len(s)):
            
            freq[s[right]] = freq.get(s[right],0) + 1  # Frequency of a character
            
            max_freq = max(max_freq, freq[s[right]])
            
            if right - left + 1 - max_freq > k:  # shrining starts
            
                freq[s[left]] -= 1
                
                left += 1
                
            res = max(res, right - left + 1)
            
        return res
                
            