'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def solve(self,root,move):
        if root == None:
            return 0
            
        l = self.solve(root.left,move)
        r = self.solve(root.right,move)
        
        excess = (l+r+root.data) - 1
        move[0] += abs(l) + abs(r)
        
        return excess
        
    def distCandy(self, root):
        # code here
        move = [0]
        self.solve(root,move)
        
        return move[0]
        