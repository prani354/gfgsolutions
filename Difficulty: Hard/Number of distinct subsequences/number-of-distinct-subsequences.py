class Solution:
	def distinctSubseq(self, str):
		# code here
		n = len(str)
		MOD = 10**9  + 7
		
		dp = [0] * (n+1)
		dp[0] = 1  # empty string
		
		last = [-1] * 26 #character repetition
		
		for i in range(1,n+1):
		    ch = s[i-1]
		    dp[i] = (2 * dp[i-1]) % MOD  #each character subsequence
		    
		    prev = last[ord(ch) - ord('a')]
		    
		    if prev != -1:
		        dp[i] = (dp[i] - dp[prev]) % MOD  #subsequence formation
		        
		    last[ord(ch) - ord('a')] = i - 1  #index updation
		    
		return dp[n]
		        
		  
		    
		    