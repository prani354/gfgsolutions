class Solution:
	def countStrings(self,n):
    	# code here
    	if n == 1:
    	    return 2
    	    
    	first , second = 1, 1
    	
    	for _ in range(2,n+1):
    	    
    	    f = first + second
    	    s = first
    	    
    	    first , second = f, s
    	    
    	return first + second
    	