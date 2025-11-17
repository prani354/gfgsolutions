class Solution:
	def maxSumIS(self, arr):
		# code here
		n = len(arr)
		
		dp = arr[:] #copy of array
		
		for i in range(n):
		    for j in range(i):
		        
		        if arr[i] > arr[j]:
		            dp[i] = max(dp[i],dp[j] + arr[i])
		            
		            
		return max(dp)
		            