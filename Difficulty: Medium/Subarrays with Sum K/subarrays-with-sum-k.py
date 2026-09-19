class Solution:
    def cntSubarrays(self, arr, k):
        # code here
        count = 0
        curr_sum = 0
        
        counter = {0:1}
        
        for num in arr:
            
            curr_sum += num
            
            rem = curr_sum - k
            
            if rem in counter:
                count += (counter[rem])
                
            counter[curr_sum] = counter.get(curr_sum,0) + 1
            
        return count