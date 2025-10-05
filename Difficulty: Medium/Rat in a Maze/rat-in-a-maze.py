class Solution:
    def ratInMaze(self, maze):
        # code here
        
        def safe(x,y):
            
            return 0 <= x < n and 0 <= y < n and maze[x][y] == 1 and not visited[x][y]
            
        def solve(x,y,path):
            
            #base case
            if x == n-1 and y == n-1:
                res.append(path)
                return
            
            visited[x][y] = True
            
            for nx,ny,move in [(1,0,'D') , (0,-1,'L'),(0,1,'R'),(-1,0,'U')]:
                dx , dy = x+nx , y+ny
                
                if safe(dx,dy):
                    solve(dx,dy,path+move)
                    
            #Bactrack by marking it as unvisited
            
            visited[x][y] = False
            
        if maze[0][0] == 0:
            return []
            
        res = []
        n = len(maze)
        visited = [[False] * n for _ in range(n)]
            
        solve(0,0,"")
        return sorted(res)