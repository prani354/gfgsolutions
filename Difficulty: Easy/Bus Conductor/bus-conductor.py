class Solution:
    def findMoves(self, chairs, passengers):
        # code here
        chairs.sort()
        passengers.sort()
        
        n = len(chairs)
        res = 0
        
        for i in range(n):
            res += abs(chairs[i] - passengers[i])
            
        return res
        
