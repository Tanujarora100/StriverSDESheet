package Graph;

public class SurroundedRegions {
public void solve(char[][] grid) {
    if (grid.length < 2 || grid[0].length < 2) { // If the grid is too small, return
        return;
    }

    int n = grid.length; // Number of rows
    int m = grid[0].length; // Number of columns

    // Traverse the border of the grid and mark connected 'O's with '#'
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if ((i == 0 || j == 0 || i == n - 1 || j == m - 1) && grid[i][j] == 'O') {
                dfsOne(i, j, grid); // Depth-first search to mark connected 'O's
            }
        }
    }

    // Restore the grid: 'O's inside the border are marked as 'X', '#' are restored to 'O'
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 'O') {
                grid[i][j] = 'X'; // Mark 'O' inside the border as 'X'
            }
            if (grid[i][j] == '#') {
                grid[i][j] = 'O'; // Restore '#' to 'O'
            }
        }
    }
}

// Depth-first search to explore the grid and change 'O' to '#'
private void dfsOne(int i, int j, char[][] grid) {
    // Base case: out of bounds or not an 'O'
    if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] != 'O') {
        return;
    }
    // Change the current 'O' to '#'
    grid[i][j] = '#';
    // Explore the adjacent cells
    dfsOne(i - 1, j, grid); // Up
    dfsOne(i + 1, j, grid); // Down
    dfsOne(i, j - 1, grid); // Left
    dfsOne(i, j + 1, grid); // Right
}
}
