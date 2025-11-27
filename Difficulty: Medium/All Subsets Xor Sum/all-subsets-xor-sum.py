class Solution:
    def subsetXORSum(self, arr):
        # code here
        Or = 0
        
        for num in arr:
            Or |= num
            
        return Or* (1 << (len(arr) - 1))