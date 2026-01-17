class Solution():
    def checkRedundancy(self, s):
        # code here 
        stack = []
        operators = set(['+', '-', '*', '/'])
        
        for c in s:
            
            if c == ')':
                op = False
                
                while stack and stack[-1] != '(':
                    if stack[-1] in operators:
                        op = True
                        
                    stack.pop()
                    
                stack.pop()
                
                if not op:
                    return True
                
            else:
                stack.append(c)
                
        return False
            