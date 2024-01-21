from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                
                # count number of live neighbours
                live_neighbours = 0
                for x in range(max(i-1, 0), min(i+2, m)):
                    for y in range(max(j-1, 0), min(j+2, n)):
                        if i == x and j == y:
                            continue
                        live_neighbours += board[x][y] % 2
                
                # mark the cell if it needs to change states
                if board[i][j] == 0:
                    if live_neighbours == 3:
                        board[i][j] = 2
                elif live_neighbours < 2 or live_neighbours > 3:
                    board[i][j] = 3
        
        # change all required states
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0