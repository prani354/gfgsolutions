class Solution:
    def josephus(self, n, k):
        # code here
        survivor = 0
        
        for i in range(2,n+1):
            survivor = (survivor+k) % i
            
        return survivor + 1