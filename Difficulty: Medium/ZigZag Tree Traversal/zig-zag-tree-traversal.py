'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def zigZagTraversal(self, root):
        # code here
        
        if not root:
            return []
            
        flag = True
        q = deque([(root)])
        res = []

        while q:
            n = len(q)
            ans = []
            
            for _ in range(n):
                
                node = q.popleft()
                ans.append(node.data)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            if flag:
                res.extend(ans)
                flag = False
            else:
                res.extend(reversed(ans))
                flag = True
                
                
        return res
                
                
                
                
                
                
            
            