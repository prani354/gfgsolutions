class Solution:
    def kokoEat(self, arr, k):
        # Code here
        l = 1
        r = max(arr)
        ans = r
        
        while l <= r:
            
            hours = 0
            mid = (l + r) // 2
            
            for banana in arr:
                hours += math.ceil(banana/mid)
                
            if hours <= k:
                ans = mid
                r = mid - 1
                
            else:
                l = mid + 1
                
        return ans
        