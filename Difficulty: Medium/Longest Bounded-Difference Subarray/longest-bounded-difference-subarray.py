from collections import  deque
class Solution:
    def longestSubarray(self, arr, x):
        #code here
        n = len(arr)
        l = 0
        max_len = 0
        start_idx= 0
        min_dq , max_dq = deque(),deque()
        
        for r in range(n):
            
            while min_dq and arr[r] < arr[min_dq[-1]]:
                min_dq.pop()
            min_dq.append(r)
            
            while max_dq and arr[r] > arr[max_dq[-1]]:
                max_dq.pop()
            max_dq.append(r)
            
            while arr[max_dq[0]] - arr[min_dq[0]] > x:
                if min_dq[0] == l:
                    min_dq.popleft()
                if max_dq[0] == l:
                    max_dq.popleft()
                    
                l += 1
                
            if r - l + 1 > max_len:
                max_len = r - l + 1
                start_idx = l
                
        return arr[start_idx:start_idx+max_len]
            
        