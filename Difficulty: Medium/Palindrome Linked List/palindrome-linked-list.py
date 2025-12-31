
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Solution:
    def isPalindrome(self, head):
        # code here
        
        slow = head
        fast = head
        
        #Middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #Reverse the list from the middle
        prev = None
        curr = slow
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        #middle and head are traversed to check teh palindrome
        while prev:
            if head.data != prev.data:
                return False
                
            head = head.next
            prev = prev.next
            
        return True
            
            
        
        