'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

'''

class Solution:
    def constructTree(self, pre, post):
        # code here
        post_index = {val: i for i, val in enumerate(post)}  # Map for quick index lookup
        
        def build(preL, preR, postL, postR):
            if preL > preR:
                return None
            root = Node(pre[preL])
            if preL == preR:
                return root

            # Next value in pre[] is the left child
            left_root_val = pre[preL + 1]
            idx = post_index[left_root_val]
            left_size = idx - postL + 1

            # Recursively build left and right subtrees
            root.left = build(preL + 1, preL + left_size, postL, idx)
            root.right = build(preL + left_size + 1, preR, idx + 1, postR - 1)
            return root
        
        return build(0, len(pre) - 1, 0, len(post) - 1)