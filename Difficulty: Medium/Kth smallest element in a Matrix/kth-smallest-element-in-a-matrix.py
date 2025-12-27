import heapq
class Solution:
    def kthSmallest(self, mat, k):
        # code here
        res = []
        
        for i in mat:
            for num in i:
                res.append(num)
                
        res.sort()
        return res[k-1]