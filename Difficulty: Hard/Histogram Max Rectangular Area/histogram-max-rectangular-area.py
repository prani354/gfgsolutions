class Solution:
    def getMaxArea(self, arr):
        # code here
        stk = []
        max_area = 0
        n = len(arr)
        
        for i,height in enumerate(arr):
            start = i
            
            while stk and stk[-1][1] > arr[i]:
                idx,h = stk.pop()
                width = i - idx
                area = h * width
                max_area = max(max_area,area)
                start = idx
                
            stk.append((start,height))
            
        while stk:
            idx,h = stk.pop()
            width = n-idx
            area = h * width
            max_area = max(max_area,area)
            
        return max_area
                
        