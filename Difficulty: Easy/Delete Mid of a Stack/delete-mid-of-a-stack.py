class Solution:
    def deleteMid(self, stack):
        #code here
        n = len(stack)
        res = []
        if n % 2 == 0:
            mid = n // 2
            
        else:
            mid = (n + 1)//2
            
        for i in range (n):
            if i == mid - 1:
                stack.pop(i)
                
        
        return stack[::-1]
            
        
            
        