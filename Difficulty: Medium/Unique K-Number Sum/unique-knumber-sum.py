class Solution:
    def combinationSum(self, n, k):
        # code here
        res = []
        
        def backtrack(ans,curr_sum,i):
            
            if len(ans) == k and curr_sum == n:
                res.append(ans[:])
                return
            
            if len(ans) > k and curr_sum > n:
                return
            
            for num in range(i,10):
                
                #Checking the combination length is k if it is less break it
                
                if len(ans) + (9-num+1) < k:
                    break
                
                ans.append(num)
                backtrack(ans,curr_sum+num,num+1)
                ans.pop()
                
        backtrack([],0,1)
        
        return res