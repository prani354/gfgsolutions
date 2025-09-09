class Solution:
    def assignHole(self, mices, holes):
        # code here
        mices.sort()
        holes.sort()
        
        n = len(mices)
        
        res = 0
        
        for i in range(n):
            res = max(res,abs(mices[i]-holes[i]))
            
        return res
                
                
        
                
                
        