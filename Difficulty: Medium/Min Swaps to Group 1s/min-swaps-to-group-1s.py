class Solution:
    def minSwaps(self, arr):
        # code here
        n = len(arr)
        
        k = sum(arr)
        
        if k == 0:
            return -1
            
        curr_ones = sum(arr[:k])
        max_ones = curr_ones
        
        for i in range(k,n):
            
            curr_ones += arr[i]
            curr_ones -= arr[i-k]
            
            max_ones = max(max_ones,curr_ones)
            
        return k - max_ones