class Solution:
    def transpose(self, mat):
        # code here
        n = len(mat)
        
        res = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                
                res[i][j] = mat[j][i]
                
        return res
        