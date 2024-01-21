from typing import List

from Tree.BinaryTree.Easy.DiameterTree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:        
        def buildBST(nums,left,right):
            if left>right:
                return
            mid= (left+right)//2
            # Make a root of the mid element
            value= nums[mid]
            root= TreeNode(value)
            root.left= buildBST(nums,left,mid-1)
            root.right= buildBST(nums,mid+1,right)
            return root
        return buildBST(nums,0,len(nums)-1)