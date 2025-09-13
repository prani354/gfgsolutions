class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        arr = list(set(arr))
        arr.sort()
        
        if len(arr) == 1:
            return [-1]
            
        return [arr[0],arr[1]]
        
