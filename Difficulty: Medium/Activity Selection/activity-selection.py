class Solution:
    def activitySelection(self, start: list[int], finish: list[int]) -> int:
        #code here
        time = list(zip(start,finish))
        time.sort(key= lambda x:x[1])
        
        count = 1
        lf = time[0][1]
        
        for i in range(1,len(time)):
            st = time[i][0]
            
            if st > lf:
                count += 1
                lf = time[i][1]
                
        return count
        
                
        
        