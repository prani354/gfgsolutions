class Solution:
    def minParentheses(self, s):
        # code here
        open_count = 0
        close_count = 0
        
        for i in s:
            if i == "(":
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    close_count += 1
                    
        return open_count + close_count
            
                
        
        