package Graph;

import java.util.LinkedList;
import java.util.Queue;

public class NumberOfIslands {
    public boolean isValid(int x, int y, char[][] grid) {
        if (x >= 0 && y >= 0 && x < grid.length && y < grid[0].length && grid[x][y] == '1')
            return true;
        return false;
    }

    public int numIslands(char[][] grid) {
        // Array to store the four directions: up, down, right, left
        int[][] directions = new int[][] { { -1, 0 }, { 1, 0 }, { 0, 1 }, { 0, -1 } };

        int islands = 0; // Counter for the number of islands
        int n = grid.length; // Number of rows in the grid
        int m = grid[0].length; // Number of columns in the grid

        // Nested loops to iterate through each cell in the grid
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // If the cell contains land (represented by '1'), perform a breadth-first
                // search
                if (grid[i][j] == '1') {
                    bfs(i, j, grid, directions); // Call the breadth-first search function
                    islands++; // Increment the island counter
                }
            }
        }

        return islands; // Return the total number of islands
    }

    public void bfs(int i, int j, char[][] grid, int[][] directions) {
        // Initialize a queue to store the indices of the cells to be visited
        Queue<int[]> q = new LinkedList<>();
        // Add the initial cell indices to the queue
        q.offer(new int[] { i, j });
        // Process cells in the queue until it's empty
        while (!q.isEmpty()) {
            // Retrieve and remove the cell indices from the front of the queue
            int[] temp = q.poll();
            // Explore all neighboring cells based on the given directions
            for (int[] dir : directions) {
                int x = temp[0] + dir[0]; // Calculate the x-coordinate of the neighboring cell
                int y = temp[1] + dir[1]; // Calculate the y-coordinate of the neighboring cell
                // Check if the neighboring cell is within the grid and is valid
                if (isValid(x, y, grid)) {
                    // Add the neighboring cell to the queue for further exploration
                    q.offer(new int[] { x, y });
                    // Mark the neighboring cell as visited by updating the value in the grid
                    grid[x][y] = '0';
                }
            }
        }
    }
    /*
     * Time complexity: O(m*n) where m is the number of rows and n is the number of
     * columns in the grid.
     * 
     * Space complexity: O(min(m,n)) where m is the number of rows and n is the
     * number of columns in the grid.
     */
}
