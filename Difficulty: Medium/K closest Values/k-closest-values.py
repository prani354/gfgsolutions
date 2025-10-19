'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getKClosest(self, root, target, k):
        # code here
        import heapq
        ret=[(-float('inf'),float('inf'),)]*k
        def dfs(cur=root):
            nonlocal target
            if not cur:
                return
            dfs(cur.left)
            if -ret[0][0]<=abs(cur.data-target):
                return
            heapq.heapreplace(ret,(-abs(cur.data-target),cur.data,))
            dfs(cur.right)
        dfs()
        ret=[x[1] for x in ret]
        return ret
        
    