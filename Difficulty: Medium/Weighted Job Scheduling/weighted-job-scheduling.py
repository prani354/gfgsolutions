class Solution: 
    def maxProfit(self, jobs):
        # code here
        jobs.sort(key = lambda x:x[1])
        n = len(jobs)
        
        end_time = [job[1] for job in jobs]
        
        dp = [0] * n
        dp[0] = jobs[0][2]
        
        def non_overlap(idx):   #to find non_overlap
            l,h = 0 , idx - 1   
            
            while l <= h:
                m = (l+h) // 2
                
                if jobs[m][1] <= jobs[idx][0]:
                    if jobs[m+1][1] <= jobs[idx][0]:
                        l = m+1
                    else:
                        return m
                        
                else:
                    h = m-1
                    
            return -1  #return index
            
        for i in range(1,n):  #building dp table
            initial_profit = jobs[i][2]
            non_lap = non_overlap(i)
            
            if non_lap != -1:
                initial_profit += dp[non_lap]
                
            dp[i] = max(dp[i-1],initial_profit)
            
        return dp[-1]
