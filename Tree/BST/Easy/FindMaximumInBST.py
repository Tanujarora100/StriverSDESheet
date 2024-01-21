#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def findMax(self,root):
        #code here
        while root.right is not None:
            root=root.right
        return root.data
    def findMin(self,root):
        #code here
        while root.left is not None:
            root=root.left
        return root.data
