class Solution:
    def maxProfit(self, arr, k):
        # Code here
        if not arr:
            return 0
            
        hold = -arr[0]
        cash = 0
        
        for price in arr[1:]:
            
            prev_hold = hold
            
            hold = max(hold,cash - price)
            
            cash = max(cash, prev_hold + price - k)
            
        return cash