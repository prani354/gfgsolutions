'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def removekeys(self, root, l, r):
        #code here
        
        def dfs(root):
            nonlocal l , r
            curr = root
        
            if not root :
                return None
                
            if l <= curr.data <= r:
                curr.left = dfs(curr.left)
                curr.right = dfs(curr.right)
                return curr
                
            if curr.data < l:
                return dfs(curr.right)
                
            if curr.data > r:
                return dfs(curr.left)
                
        return dfs(root)
        
        