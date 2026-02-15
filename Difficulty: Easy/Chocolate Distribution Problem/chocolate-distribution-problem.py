#User function Template for python3
#from collections import deque
class Solution:

    def findMinDiff(self, arr,M):

        # code here
        arr.sort()
        n = len(arr)
        min_val = float('inf')
        
        for i in range(n - M + 1):
            diff = arr[i+(M-1)] - arr[i]
            min_val = min(min_val,diff)
            
        return min_val
            
            
            
        
        
        
        
        
        
        