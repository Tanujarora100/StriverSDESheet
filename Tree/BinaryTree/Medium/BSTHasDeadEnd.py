class Solution:
    def solve(self, root, mini, maxi):
        if root == None:
            return False
            
        if mini == maxi:
            return True
            
        left_side = self.solve(root.left, mini, root.data-1)
        right_side = self.solve(root.right, root.data+1, maxi)
            
        return left_side or right_side
        
    def isDeadEnd(self, root):
        return self.solve(root, 1, float('inf'))