class Solution:
    def nextGreater(self, arr):
        # code here
        stk = []
        n = len(arr)
        narr = arr+arr
        res = [-1] * n
        
        for i in range(len(narr)):
            while stk and narr[stk[-1]] < narr[i]:
                idx = stk.pop()
                idx %= n
                res[idx] = narr[i]
            stk.append(i)
            
        return res
                    
                    
        