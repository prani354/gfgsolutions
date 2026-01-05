class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        #curr_sum = 0 
        count_sum = res = sum(arr[:k])
        
        for i in range(k,len(arr)):
            count_sum = count_sum - arr[i-k] + arr[i]
            res = max(count_sum,res)
            
        return res