import heapq
class Solution:
    def kClosest(self, points, k):
        # code here
        heap = []
        res = []
        d = {}
        
        
        for num in points:
            x2,y2 = num
            dist = (x2**2 + y2 **2)
            d[dist] = num
            
            heapq.heappush(heap,dist)
            
        for _ in range(k):
            res.append(d[heapq.heappop(heap)])
        
        return res
            
            
        
            
            
            
            
        
        
        