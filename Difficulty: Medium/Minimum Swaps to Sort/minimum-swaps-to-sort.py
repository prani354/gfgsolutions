class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, arr):
		#Code here
		n = len(arr)
		
		arr_pos = [(value,key) for key,value in enumerate(arr)]
		
		arr_pos.sort(key = lambda x:x[0])  #si=orting based on value 
		
		visited = [False] * n
		swap = 0
		
		for i in range(n):
		    
		    if visited[i] or arr_pos[i][1] == i:  #already correctly placed or visited
		        continue 
		    
		    j = i
		    cycle = 0
		    
		    while not visited[j]:
		        
		        visited[j] = True
		        j = arr_pos[j][1]  #moving to next index
		        cycle += 1
		        
		    if cycle > 0:
		        swap += (cycle - 1)   #total swap at each cycle
		        
	    return swap