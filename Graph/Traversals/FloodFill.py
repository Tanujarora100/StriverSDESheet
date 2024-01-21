class Solution:
    def dfs(self, image, i, j, val, newColor):
        if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] == newColor or image[i][j] != val:
            return
        image[i][j] = newColor
        self.dfs(image, i - 1, j, val, newColor)
        self.dfs(image, i + 1, j, val, newColor)
        self.dfs(image, i, j - 1, val, newColor)
        self.dfs(image, i, j + 1, val, newColor)
    
    def floodFill(self, image, sr, sc, newColor):
        val = image[sr][sc]
        self.dfs(image, sr, sc, val, newColor)
        return image