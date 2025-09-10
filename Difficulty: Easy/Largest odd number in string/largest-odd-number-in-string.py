#User function Template for python3

class Solution:
    def maxOdd(self, s):
        s = list(s)
        max_val = float('-inf')
        add = ""
        for i in range(len(s)):
            add += s[i]
            
            if int(add) % 2 != 0:
                max_val = max(max_val,int(add))
                
                
        if max_val == float('-inf'):
            return ""
            
        return str(max_val)
        
       
                