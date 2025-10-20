class Solution:
    def countBSTs(self, arr):
        # Code here
        #catalan numbers
        n = len(arr)
        cat = [0] * (n+1)
        
        cat[0] = cat[1] = 1
        
        for i in range(2,n+1):
            for j in range(i):
                cat[i] += cat[j] * cat[i-j-1]
                
        s_arr = sorted(arr)
        res = []
        
        for num in arr:
            idx = s_arr.index(num)
            left_count = idx
            right_count =  n - idx - 1
            
            res.append(cat[left_count] * cat[right_count])
            
        return res
            
        