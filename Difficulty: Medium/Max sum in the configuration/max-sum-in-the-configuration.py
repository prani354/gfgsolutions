class Solution:
    def maxSum(self, arr): 
        # Code here
        
        arr_sum = sum(arr)
        no_rotate = 0
        
        for i in range(len(arr)):
            no_rotate += (i * arr[i])
            
        
        max_sum = no_rotate
        curr_sum = no_rotate
        
        for k in range(1,len(arr)):
            # rotation using simple method 
            curr_sum += (arr_sum - len(arr) * arr[len(arr) - k])
            max_sum = max(max_sum,curr_sum)
            
        return max_sum