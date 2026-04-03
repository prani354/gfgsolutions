class Solution:
    def diagView(self, mat): 
    # code here 
        n = len(mat)
    
        res = []
    
        for s in range(2 * n - 1):
        
            for i in range(n):
            
                j = s - i
            
                if 0 <= j < n:
                    res.append(mat[i][j])
                
        return res