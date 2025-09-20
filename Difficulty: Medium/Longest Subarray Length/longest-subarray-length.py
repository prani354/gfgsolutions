class Solution:
    def longestSubarray(self, arr):
        # code here
        n = len(arr)
        stk = []
        left_arr = [-1] * n
        
        for i in range(n-1,-1,-1): #from right to left
        
            while stk and arr[stk[-1]] < arr[i]:
                left_arr[stk.pop()] = i
            stk.append(i)
            
        stk = []
        right_arr = [n] * n
        
        for i in range(n): #from left to right
            
            while stk and arr[stk[-1]] < arr[i]:
                right_arr[stk.pop()] = i
                
            stk.append(i)
            
        res = 0
        
        for i in range(n):
            l = right_arr[i] - left_arr[i] - 1
            v = arr[i]
            
            if l >= v:
                res = max(res,l)
                
        return res
                
        