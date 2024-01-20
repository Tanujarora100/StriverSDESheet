#User function Template for python3
from collections import defaultdict,deque
class Solution:
    def minTime(self, root,start):
        # code here
        parent_map = {}
        # There are no duplicates in the tree so we can build a hash_map

        def buildParentMap(node, parent, parentMap):
            if node is None:
                return
            parentMap[node] = parent
            buildParentMap(node.left, node, parentMap)
            buildParentMap(node.right, node, parentMap)
        buildParentMap(root, None, parent_map)
        minimum_time = 0

        def find_target(root, target):
            if root is None:
                return
            if root.data == target:
                return root

            left_subtree = find_target(root.left, target)
            right_subtree = find_target(root.right, target)

            if left_subtree:
                return left_subtree

            if right_subtree:
                return right_subtree
            # No Sub tree with the dataue found
            return None
        target_node = find_target(root, start)
        # visited=set()

        if target_node is None:
            return 0

        def bfs():
            queue = deque()
            visited = defaultdict(bool)
            ans = 0
            queue.append(target_node)
            visited[target_node] = True
            while queue:
                size = len(queue)
                flag = False
                for _ in range(size):
                    curr_node = queue.popleft()
                    if curr_node.left and not visited.get(curr_node.left):
                        visited[curr_node.left] = True
                        queue.append(curr_node.left)
                        flag = True
                    if curr_node.right and not visited.get(curr_node.right):
                        visited[curr_node.right] = True
                        flag = True
                        queue.append(curr_node.right)
                    if parent_map[curr_node] and not visited.get(parent_map[curr_node]):
                        visited[parent_map[curr_node]] = True
                        flag = True
                        queue.append(parent_map[curr_node])
                if flag:
                    ans += 1
            return ans
        ans = bfs()
        return ans


