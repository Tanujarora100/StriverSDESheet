#User function Template for python3

class Solution:
    def findPath(self, maze, n):
        ROWS = len(maze)
        COLS=len(maze[0])
        visited= [[False]*COLS for _ in range(ROWS)]
        ansList=[]
        if maze[0][0]==0:
            return []
            # Start is invalid
        def dfs(i ,j ,visited,path):
            
            if i==ROWS-1 and j==COLS -1 and maze[i][j]!=0:
                ansList.append(path)
                return
            if i<0 or j<0 or i>=ROWS or j>=COLS or visited[i][j] or maze[i][j]==0:
                
                return
                # Case handled for End Invalid
            visited[i][j]=True
            dfs(i+1,j,visited,path+"D")
            dfs(i-1,j,visited,path+"U")
            dfs(i,j+1,visited,path+"R")
            dfs(i,j-1,visited,path+"L")
            visited[i][j]=False
            path=path[:-1]
        dfs(0,0,visited,"")
        return ansList
