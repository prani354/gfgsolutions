class Solution:
    def possibleWords(self, arr):
        # code here
        d = [[""],[""],"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        n = len(arr)
        ans = []
        res = []
        
        def backtrack(i):
            if i == n:
                res.append("".join(ans))
            else:
                for c in d[arr[i]]:
                    ans.append(c)
                    backtrack(i+1)
                    ans.pop()
                    
        backtrack(0)
        
        return res
