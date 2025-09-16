class Solution:
    def evaluatePostfix(self, arr):
        # code here
        stk = []
        
        for c in arr:
            
                
            if c == "+" or c == "-" or c == "*" or c == "/" or c == "^":
                
                x = stk.pop()
                y = stk.pop()
                
                if c == "+":
                    stk.append(y+x)
                elif c == "-":
                    stk.append(y-x)
                elif c == "*":
                    stk.append(y*x)
                elif c == "/":
                    stk.append(int(y // x))
                else:
                    stk.append(int(y ** x))
                    
            else:
                stk.append(int(c))
                    
                    
        return stk[-1]
                
        