'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        # code here
        if not root:
            return []
            
        return self.postOrder(root.left) + self.postOrder(root.right) + [root.data]
        
    
        