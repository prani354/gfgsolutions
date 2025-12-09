class Solution:
    def findDuplicates(self, arr):
        # code here
        hashset = set()
        res = []
        
        for num in arr:
            if num in hashset:
                res.append(num)
                
            hashset.add(num)
                
        return res
        