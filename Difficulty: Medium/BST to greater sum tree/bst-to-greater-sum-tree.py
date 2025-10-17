'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def transformTree(self, root):
        # code here
        sum = 0
        
        def dfs(curr = root):
            nonlocal sum
            
            if not curr:
                return 0
            
            #Reverse Inorder traversal     
            dfs(curr.right)
            #Swapping the sum value
            curr.data , sum = sum , curr.data+sum
            
            dfs(curr.left)
            
        dfs(root)
        
        return root
        
