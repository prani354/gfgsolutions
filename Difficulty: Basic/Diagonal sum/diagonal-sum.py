#User function Template for python3

class Solution:
	def DiagonalSum(self, matrix):
		# Code here
		n= len(matrix)
		m = len(matrix[0])
		tot = 0
		
	    for i in range(n):
	        for j in range(m):
	            
	            if i == j:
	                tot += matrix[i][j]
	                
	            if i+j == n-1:
	                tot += matrix[i][j]
	                
	    return tot