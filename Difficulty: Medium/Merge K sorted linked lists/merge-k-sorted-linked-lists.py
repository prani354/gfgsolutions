'''
class Node:
    def _init_(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def mergeKLists(self, arr):
        # code here
        ans = []
        
        for head in arr:
            temp = head
            
            while temp:
                ans.append(temp.data)
                temp = temp.next
                
        ans.sort()
        
        head = Node(ans[0])
        temp = head
        
        for num in ans[1:]:
            curr = Node(num)
            temp.next = curr
            temp = temp.next
            
        temp.next = None
        
        return head
        
        