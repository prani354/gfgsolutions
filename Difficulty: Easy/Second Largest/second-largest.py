import heapq
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        k = 2
        heap = []
        l = list(set(arr))
        if len(l) == 1:
            return -1
        for num in l:
            
            heapq.heappush(heap,num)
            
            if len(heap) > k:
                heapq.heappop(heap)
                
        return heap[0]
                
        
        