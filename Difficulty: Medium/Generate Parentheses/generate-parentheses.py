#User function Template for python3

class Solution:
    def generateParentheses(self, n):
        #code here
        n = n//2
        
        res = []
        
        def backtrack(l,oc,cc):
            
            if oc == n and cc == n:
                res.append("".join(l))
                return
            
            if oc < n:
                l.append("(")
                backtrack(l,oc+1,cc)
                l.pop()
                
            if cc < oc:
                l.append(")")
                backtrack(l,oc,cc+1)
                l.pop()
                
        backtrack([],0,0)
        
        return res
        
        
