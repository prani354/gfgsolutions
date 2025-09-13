#User function Template for python3

class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        #Your code here
        res = 0
        alt = 0
        for i in range(1,len(arr)):
            
            if arr[i] > arr[i-1]:
                alt += 1
                
            else:
                alt = 0
                
            res = max(res,alt)
            
        return res
            
                
            
                
                
                