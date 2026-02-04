class Solution:
    def getLastMoment(self, n, left, right):
        # code here
        max_time = 0
        
        for p in left:
            max_time = max(max_time,p)
            
        for p in right:
            max_time = max(max_time,n-p)
            
        return max_time
            
        