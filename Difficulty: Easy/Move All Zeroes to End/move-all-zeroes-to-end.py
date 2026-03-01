class Solution:
	def pushZerosToEnd(self, arr):
    	# code here
    	j = 0
    	
    	for i in range(len(arr)):
    	    
    	    if arr[i] != 0:
    	        arr[j],arr[i] = arr[i],arr[j]  #swapping elements when they pass teh condition arr[i] != 0
    	        j += 1
    	        
    	return arr