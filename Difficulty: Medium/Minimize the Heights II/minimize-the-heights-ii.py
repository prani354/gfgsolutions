class Solution:
    def getMinDiff(self, arr, k):
        # code here
        arr.sort()
        
        if len(arr) == 1:
            return 0
            
        res = arr[len(arr)-1] - arr[0]
        
        small = arr[0] + k
        large = arr[len(arr)-1] - k
        
        for i in range(len(arr)-1):
            
            min_height = min(small,arr[i+1]-k)
            max_height = max(large,arr[i]+k)
            
            if min_height < 0:
                continue
            
            res = min(max_height-min_height,res)
            
        return res
            
        