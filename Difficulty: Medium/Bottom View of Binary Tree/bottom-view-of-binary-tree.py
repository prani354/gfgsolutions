
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

from collections import deque
class Solution:
    def bottomView(self, root):
        # code here
        
        if not root:
            return []
            
        q = deque([(root,0)]) #node and horizontal distance
        
        hd_map = {}
        
        while q:
            
            node,hd = q.popleft()
            hd_map[hd] = node.data
            
            if node.left:
                q.append((node.left,hd-1))
                
            if node.right:
                q.append((node.right,hd+1))
                
        return [hd_map[x] for x in sorted(hd_map.keys())]
        