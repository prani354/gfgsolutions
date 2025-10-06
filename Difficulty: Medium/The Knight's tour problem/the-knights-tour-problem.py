class Solution:
    def knightTour(self, n):
        # code here
        moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        
        board = [[-1 for _ in range(n)] for _ in range(n)]
        
        board[0][0] = 0
        
        def valid(x,y):
            return 0 <= x < n and 0 <= y < n and board[x][y] == -1
            
        def backtrack(x,y,step):
            
            if step == n * n:
                return True
                
            for dx,dy in moves:
                nx,ny = x+dx , y+dy
                
                if valid(nx,ny):
                    board[nx][ny] = step  #No of cells visited mentioned here
                    
                    if backtrack(nx,ny,step+1):
                        return True
                        
                    board[nx][ny] = -1  #backtrack
                    
            return False
            
       
        
        if backtrack(0,0,1):
            return board
        else:    
            return []
            
        
        