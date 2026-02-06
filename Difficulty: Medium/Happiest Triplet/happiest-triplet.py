class Solution:
    def smallestDiff(self,a, b, c):
        #code here.
    
        a.sort()
        b.sort()
        c.sort()
        
        
        i = j = k  = 0 
        n = len(a)
        
        min_diff = float('inf')
        min_sum = float('inf')
        ans = []
        
        while i < n and j < n and k < n:
            
            x,y,z = a[i],b[j],c[k]
            
            curr_max = max(x,y,z)
            curr_min = min(x,y,z)
            diff = curr_max - curr_min
            s = x+y+z
            
            if diff < min_diff or (diff == min_diff and s < min_sum):
                min_diff = diff
                min_sum = s
                ans = [x,y,z]
                
            if curr_min == x:
                i += 1
                
            elif curr_min == y:
                j += 1
                
            else:
                k += 1
                
        return sorted(ans, reverse = True)
            
            
