class Solution:
    def minMen(self, arr):
        #code here 
        n = len(arr)
    
    # Convert entries into intervals
        intervals = []
        for i, val in enumerate(arr):
            if val != -1:
                left = max(0, i - val)
                right = min(n - 1, i + val)
                intervals.append((left, right))
        
        # Sort by start then by end descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        current_end = 0
        idx = 0
        best_reach = -1
        
        while current_end < n:
            # Try to extend coverage from intervals that start <= current_end
            while idx < len(intervals) and intervals[idx][0] <= current_end:
                best_reach = max(best_reach, intervals[idx][1])
                idx += 1
            
            # If we cannot extend further
            if best_reach < current_end:
                return -1
            
            # Pick the best interval
            count += 1
            current_end = best_reach + 1  # move to next uncovered index
    
            # If already covered everything
            if current_end >= n:
                return count
        
        return count