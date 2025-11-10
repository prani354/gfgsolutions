#User function Template for python3

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        # code here
        
        n = len(arr1)
        
        if n == 0:
            return 0
            
        if n > len(arr2):
            arr1 , arr2 = arr2, arr1
            n = len(arr1)
            
        l , h = 0 , n
        
        #binary search
        
        while l <= h:
            
            curr1 = (l + h) // 2
            curr2 = n - curr1   #length of 2n - n
            
            l1 = float('-inf') if curr1 == 0 else arr1[curr1-1]
            l2 = float('-inf') if curr2 == 0 else arr2[curr2-1]
            
            r1 = float('inf') if curr1 == n else arr1[curr1]
            r2 = float('inf') if curr2 == n else arr2[curr2]
            
            if l1 <= r2 and l2 <= r1:
                return max(l1,l2) + min(r1,r2)
                
            elif l1 > r2:
                h = curr1 - 1
                
            else:
                l = curr1 + 1
                
            
                
            
            