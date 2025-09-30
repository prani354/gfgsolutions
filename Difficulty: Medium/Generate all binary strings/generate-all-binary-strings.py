class Solution:
    def binstr(self, n):
        # code here
        res = []
        
        for i in range((2**n)):
            res.append(bin(i)[2:].zfill(n))
            
        return res
        