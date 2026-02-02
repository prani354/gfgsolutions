class Solution:
    def maxCircularSum(self, arr):
        # code here
        n = len(arr)
        if n == 0:
            return 0
            
        def kadane_max(arr):
            curr_sum = max_sum = arr[0]
            for num in arr[1:]:
                curr_sum = max(num , curr_sum+num)
                max_sum = max(max_sum , curr_sum)
                
            return max_sum
        
        def kadane_min(arr):
            curr_sum = max_sum = arr[0]
            for num in arr[1:]:
                curr_sum = min(num , curr_sum+num)
                max_sum = min(max_sum , curr_sum)
                
            return max_sum
            
        min_wrap = kadane_min(arr)
        max_wrap = kadane_max(arr)
        
        total = sum(arr)
        
        if max_wrap < 0:
            return max_wrap
            
        tot_sum = total - min_wrap
        
        return max(tot_sum , max_wrap)
        