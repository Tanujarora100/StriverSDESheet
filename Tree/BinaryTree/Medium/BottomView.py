#User function Template for python3

from collections import deque


class Solution:
    def bottomView(self, root):
        if root is None:
            return []
            
        queue = deque()
        queue.append([root, 0])
        hashmap = {}
        minn, maxx = 0, 0
        
        while queue:
            temp = queue.popleft()
            node = temp[0]
            height = temp[1]
                #Keep updating the value again and again for bottom view.
            hashmap[height] = node.data
            if node.left:
                  queue.append([node.left, height-1])
                  minn = min(minn, height - 1)
        
            if node.right:
                  queue.append([node.right, height+1])
                  maxx = max(maxx, height+1)
            
        ans = []
        for i in range(minn, maxx+1):
            ans.append(hashmap[i])
        return ans
