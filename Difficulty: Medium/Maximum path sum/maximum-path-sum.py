'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxSum(self, root): 
        # code here
        self.max_sum = float('-inf')  

        def dfs(node):
            if not node:
                return 0  # base case

           
            left_gain = max(dfs(node.left), 0)   
            right_gain = max(dfs(node.right), 0)

            
            current_max = node.data + left_gain + right_gain

            
            self.max_sum = max(self.max_sum, current_max)

            
            return node.data + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum
            
            