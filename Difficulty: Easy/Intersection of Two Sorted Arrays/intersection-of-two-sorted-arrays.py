class Solution:
    def intersection(self,a, b):
        # code here
        s1 = set(a)
        s2 = set(b)
        
        res = s1.intersection(s2)
        
        return sorted(res)
        
        