class Solution:
    def findPeakGrid(self, mat):
        # code here
        n = len(mat)
        m = len(mat[0])
        
        left , right = 0 , m - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            max_row = max(range(n), key = lambda x:mat[x][mid])
            
            #marking infinity to the first row and last row
            left_val = mat[max_row][mid - 1] if mid > 0 else float('-inf')
            right_val = mat[max_row][mid + 1] if mid < m - 1 else float('-inf')
            
            if mat[max_row][mid] >= left_val and mat[max_row][mid] >= right_val:  #peak elemnet
                return [max_row,mid]
            elif left_val > mat[max_row][mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        return [-1,-1]