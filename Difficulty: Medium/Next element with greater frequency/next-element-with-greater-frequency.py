from collections import Counter
class Solution:
    def nextFreqGreater(self, arr):
        # code here
        n = len(arr)
        counter = Counter(arr)
        
        ans = [-1] * n
        stack = []
        for i in range(n):
            
            while stack and counter[arr[i]] > counter[arr[stack[-1]]]:
                idx = stack.pop()
                ans[idx] = arr[i]
                
            stack.append(i)
            
        return ans
                
            
        
        