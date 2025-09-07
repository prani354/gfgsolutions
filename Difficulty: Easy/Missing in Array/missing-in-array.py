class Solution:
    def missingNum(self, arr):
        # code here
        res = [-1] * (len(arr) + 2)
        
        for num in arr:
            res[num] = num
            
        for i in range(1,len(res)):
            if res[i] == -1:
                return i
                