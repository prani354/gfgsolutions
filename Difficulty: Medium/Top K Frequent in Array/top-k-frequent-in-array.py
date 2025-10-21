import heapq
class Solution:
	def topKFreq(self, arr, k):
		# Code here
		counter = Counter(arr)
		heap = []
		
		for key,value in counter.items():
		    
		     heapq.heappush(heap,(value,key))
		     
		     if len(heap) > k:
		        heapq.heappop(heap)
		        
		   
		result = []
		
        while heap:
            
            fr, num = heapq.heappop(heap)
            result.append((fr, num))
        
        result.sort(key=lambda x: (x[0], x[1]), reverse=True)
        
        
        return [num for (fr, num) in result]
		   
		        
	
		    
		
		
		
		