'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
import heapq
from collections import deque
class Solution:
    def kthSmallest(self, root, k): 
        # code here
        if root is None:
            return -1
            
        q = deque()
        q.append(root)
        heap = []
        
        while q:
            node = q.popleft()
            
            heapq.heappush(heap,-node.data)
            
            if len(heap) > k:
                heapq.heappop(heap)
                
            
            if node.left:
                q.append(node.left)
                
            if node.right:
                q.append(node.right)
                
            
                
        return -heap[0] if len(heap) >= k else -1
            
            
        