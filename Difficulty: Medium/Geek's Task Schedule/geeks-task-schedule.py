class Solution:
    def leastInterval(self, tasks: list[int], k: int) -> int:
        # code here
        n = len(tasks)
        
        d = {}
        
        for task in tasks:
            if task in d:
                d[task] += 1
                
            else:
                d[task] = 1
                
        max_count = 0
        max_freq = 0
        
        for ele,count in d.items():
            max_freq = max(max_freq,count)
            
        for count in d.values():
            if count == max_freq:
                max_count += 1
                
        # print(max_freq,max_count)
        
        return max(n , (max_freq-1) * (k+1) + max_count)
        
        