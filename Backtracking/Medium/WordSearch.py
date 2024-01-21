from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        visited=set()
        res=0

        def dfs(i,j,res,visited):
            if res==len(word):
                return True
            if i<0 or i>=rows or j<0 or j>=cols or (i,j) in visited or word[res]!=board[i][j]:
                return False

            visited.add((i,j))
            
            if( dfs(i+1,j,res+1,visited) 
            or dfs(i-1,j,res+1,visited)
             or dfs(i,j+1,res+1,visited) 
             or dfs(i,j-1,res+1,visited)):
             return True
            visited.remove((i,j))

            return False
        for i in range(rows):
            for j in range(cols):
                if board[i][j]==word[0]:
                    if dfs(i,j,0,visited):
                        return True
        return False