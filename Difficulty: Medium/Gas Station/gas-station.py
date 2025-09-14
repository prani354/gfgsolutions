class Solution:
    def startStation(self, gas, cost):
        #  code here
        if sum(gas) < sum(cost):
            return -1
            
        n = len(gas)
        tank = 0
        idx = 0
        
        for i in range(n):
            tank += gas[i] - cost[i]
            
            if tank < 0:
                tank,idx = 0,i+1
                
        return idx
            