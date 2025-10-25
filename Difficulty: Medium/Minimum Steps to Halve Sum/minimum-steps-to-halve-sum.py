import heapq
class Solution:
  def minOperations(self, arr):
    # code here
    steps = 0
    half = sum(arr) / 2
    heap = []
    
    for num in arr:
        heapq.heappush(heap,-num)
        
    total = sum(arr)
    while heap:
        if total <= half:
            return steps
            
        steps += 1
        value = -heapq.heappop(heap) / 2
        total = total - value
        
        heapq.heappush(heap,-value)
        
    return steps
        
    
    # while sum(arr) > half:
    #     idx = arr.index(max(arr))
    #     arr[idx] = arr[idx] / 2
    #     steps += 1
        
    # return steps
        