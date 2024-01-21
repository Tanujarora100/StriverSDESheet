# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from typing import List

from Tree.BinaryTree.Easy.DiameterTree import TreeNode


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        queue = [(root, 0)]
        hashmap = collections.defaultdict(list);
        level = 0
        while (len(queue)):
            levelSize = len(queue)
            while (levelSize > 0):
                curElem, pos = queue.pop(0)
                hashmap[pos].append((level, curElem.val));
                
                if (curElem.left):
                    queue.append((curElem.left, pos-1))
                
                if (curElem.right):
                    queue.append((curElem.right, pos+1));
                    
                levelSize-=1;
            level+=1;
        keys = sorted(hashmap.keys());
        result = []
            
        for key in keys:
            curLevelElems = hashmap[key];
            curLevelElems = sorted(hashmap[key])
            result.append(list(map(lambda x: x[1],curLevelElems)));
        return result