
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    
    def addTwoLists(self, head1, head2):
        # code here
        def reverse(head):
            prev = None
            curr = head
            
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            return prev
            
        r1 = reverse(head1)
        r2 = reverse(head2)
        
        carry = 0
        res = None
        
        while r1 or r2 or carry:
            x = r1.data if r1 else 0
            y = r2.data if r2 else 0
            
            s = x + y + carry
            carry = s // 10
            node = Node(s % 10)
            
            node.next = res
            res = node
            
            if r1: r1 = r1.next
            if r2: r2 = r2.next
            
        while res.data == 0:
            res = res.next
            
        return res
            
        
        