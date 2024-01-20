package Graph;

public class MaxAreaOfIsland {
    private int count = 0;

    public int maxAreaOfIsland(int[][] grid) {
        int maxarea = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    dfs(i, j, grid);
                    if (count > maxarea) {
                        maxarea = count;
                    }
                    count = 0;
                }
            }
        }
        return maxarea;
    }

    public void dfs(int i, int j, int grid[][]) {
        // Base case: if either i or j is out of bounds or the grid value at (i, j) is
        // 0, return
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] == 0) {
            return;
        }

        // Increment the count of connected cells
        count++;

        // Set the current cell as visited by marking it as 0
        grid[i][j] = 0;

        // Recursively visit the adjacent cells in the grid
        dfs(i + 1, j, grid);
        dfs(i - 1, j, grid);
        dfs(i, j - 1, grid);
        dfs(i, j + 1, grid);
    }
}
