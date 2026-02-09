class Solution:
    def findKRotation(self, arr):
        # code here
        
        x = min(arr)
        
        for num in arr:
            
            if x == num:
                return arr.index(num)