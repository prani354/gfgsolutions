class Solution:
    def maxProfit(self, arr):
        # code here
        n = len(arr)
        
        hold = [0] * n
        sell = [0] * n
        cool = [0] * n
        
        #base case
        hold[0] = -arr[0]
        sell[0] = 0
        cool[0] = 0
        
        for i in range(1,n):
            hold[i] = max(hold[i-1],cool[i-1]-arr[i])  #holding or cooled value
            sell[i] = hold[i-1] + arr[i]
            cool[i] = max(cool[i-1],sell[i-1])
            
        return max(cool[-1],sell[-1]) #profit
        