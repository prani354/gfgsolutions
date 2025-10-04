class Solution:
    def findExpr(self, s, target):
        # code here
        res = []
        
        def dfs(idx,expr,curr_val,last_opd):
            
            if idx == len(s):
                if curr_val == target:
                    res.append(expr)
                return
            
            for i in range(idx,len(s)):
                if idx != i and s[idx] == '0':
                    break
                
                curr_str = s[idx:i+1]
                num = int(curr_str)
                
                if idx == 0: #No operator at the front
                    dfs(i+1,curr_str,num,num)
                    
                else:
                    dfs(i+1,expr+"+"+curr_str,curr_val+num,num) #Additiion
                    
                    dfs(i+1,expr+"-"+curr_str,curr_val-num,-num) #subtraction
                    
                    dfs(i+1,expr+"*"+curr_str,curr_val-last_opd + last_opd*num,
                    last_opd*num) #Multiplication
                    
        dfs(0,"",0,0)
        
        return res
                    
                    
        
        