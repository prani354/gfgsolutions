class Solution:
    def uniquePerms(self, arr):
        # code here 
        arr.sort()
        ans , res = [] , []
        n = len(arr)
        hasharr = [False] * n  
        
        def backtrack():
            
            if len(ans) == n:
                res.append(ans[:])
                return
            
            prev = None
            
            for i in range(n):
                
                if hasharr[i]: #Used 
                    continue
                
                if prev is not None and prev == arr[i]: #to avoid duplicates
                    continue
                
                hasharr[i] = True
                ans.append(arr[i])
                
                backtrack()
                
                ans.pop()
                hasharr[i] = False
                
                prev = arr[i]  #to store the last element visited
                
                
        backtrack()
        return res
                
                
            
            
                
            
            