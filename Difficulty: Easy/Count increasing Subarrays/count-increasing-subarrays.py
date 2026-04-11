class Solution:
    def countIncreasing(self, arr):
        # code here.
        
        n = len(arr)
        length = 1
        count = 0
        
        for i in range(1,n):
            
            if arr[i] > arr[i-1]:
                length += 1
                
            else:
                count += (length * (length - 1)) // 2
                length = 1   #resetting the lengtn back to 1
                
        #at last the segment becomes\
        
        count += (length * (length - 1)) // 2
        
        return count