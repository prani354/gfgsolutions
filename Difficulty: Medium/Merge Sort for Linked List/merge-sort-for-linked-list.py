'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    
    def findmiddle(self,head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow= slow.next
            fast = fast.next.next 
        return slow
        
    def mergelists(self,list1,list2):
        dummy = Node(-1)
        temp = dummy
        while list1 and list2:
            if list1.data < list2.data:
                temp.next = list1
                temp = list1
                list1 = list1.next 
            else:
                temp.next = list2
                temp=list2
                list2 = list2.next 
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        return dummy.next 
        
    def mergeSort(self, head):
        # code here
        
        if  (head==None or head.next==None):
            return head
            
        middle = self.findmiddle(head)
        left = head
        right = middle.next
        middle.next = None
        
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        return self.mergelists(left,right)
        
            
       