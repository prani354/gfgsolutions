import heapq
class Solution:
   def minCost(self, arr):
    # code here
    
    if len(arr) < 2:
        return 0
        
    heap = []
    ans = 0
    res = 0
    
    for num in arr:
        heapq.heappush(heap,num)
        
    while len(heap) > 1:
        val1 = heapq.heappop(heap)
        val2 = heapq.heappop(heap)
        
        ans += val1+val2
        res += ans
        
        heapq.heappush(heap,ans)
        ans = 0
        
    return res
        
        
    
    