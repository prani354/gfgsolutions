class Solution:
    def nearlySorted(self, arr, k):  
        #code here
        import heapq
        
        heap = []
        i = 0
        
        for num in arr:
            heapq.heappush(heap,num)
            
            if len(heap) > k:
                arr[i] = heapq.heappop(heap)
                i += 1
                
        while heap:
            arr[i] = heapq.heappop(heap)
            i += 1