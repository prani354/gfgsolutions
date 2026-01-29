from collections import deque
class Solution:
	def firstNonRepeating(self, s):
		# code here
		
		freq = [0] * 26
		q = deque()
		res = []
		
		for char in s:
		    
		    freq[ord(char) - ord('a')] += 1
		    q.append(char)
		    
		    while q and freq[ord(q[0]) - ord('a')] > 1:
		        q.popleft()
		        
		    if q:
		        res.append(q[0])
		        
		    else:
		        res.append('#')
		        
		return "".join(res)
		
		
		        