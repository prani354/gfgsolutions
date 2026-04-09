#User function Template for python3


class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        count = 0
        
        i , j = 0, len(arr) - 1
        
        while i < j:
            
            
                
            if arr[i] + arr[j] > target:
                j -= 1
            
            elif arr[i] + arr[j] < target:
                i += 1
                
            else:
                
                count += 1
                
                for a in range(j-1,i,-1):
                    if arr[i] + arr[a] == target:
                        count += 1
                        
                for b in range(i+1,j):
                    if arr[j] + arr[b] == target:
                        count += 1
                i += 1
                j -= 1
                
                
        return count
