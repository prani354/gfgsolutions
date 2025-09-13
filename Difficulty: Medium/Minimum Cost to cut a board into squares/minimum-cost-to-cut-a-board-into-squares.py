class Solution:
    def minCost(self, n, m, x, y):
        # code here
        x.sort(reverse = True)
        y.sort(reverse = True)
        
        horizontal_place = 1
        vertical_place = 1
        
        i = j = 0
        total_cost = 0
        
        while i < len(x) and j < len(y):
            
            if x[i] > y[j]:
                total_cost += x[i] * horizontal_place
                vertical_place += 1
                i += 1
            
            else:
                total_cost += y[j] * vertical_place
                horizontal_place += 1
                j += 1
                
        while i < len(x):
            
            total_cost += x[i] * horizontal_place
            i += 1
            
        while j < len(y):
            
            total_cost += y[j] * vertical_place
            j += 1
            
        return total_cost
                
        
        
        
        
