class Solution:
    def minCost(self, heights, cost):
        # code here
        pairs = sorted(zip(heights, cost))
    
        # Compute total weight
        
        total_weight = sum(cost)
        half = total_weight / 2
        
        # Find weighted median
        
        cumulative = 0
        weighted_median = None
        for h, c in pairs:
            cumulative += c
            if cumulative >= half:
                weighted_median = h
                break
        
        # Compute total cost making all heights equal to weighted_median
        
        total_cost = 0
        
        for h, c in zip(heights, cost):
            total_cost += abs(h - weighted_median) * c
        
        return total_cost