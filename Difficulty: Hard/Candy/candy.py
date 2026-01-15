class Solution:
    def minCandy(self, arr):
        # Code here
        n = len(arr)
        candies = [1] * n
        
        
        for i in range(1, n):  #from the front
            if arr[i] > arr[i-1]:
                candies[i] = candies[i-1] + 1
                
       
        for i in range(n-2, -1, -1):  #from the back
            if arr[i] > arr[i+1]:
                if candies[i] <= candies[i+1]:
                    candies[i] = candies[i+1] + 1
                    
        return sum(candies)