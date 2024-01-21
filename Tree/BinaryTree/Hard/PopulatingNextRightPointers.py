from collections import deque
from typing import Optional
from xml.dom import Node


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        curr_node=root
        while curr_node.left:
            # Means we are at the last level and as we are changing the pointers from a level above the current level this level is already done and we can exit
            head=curr_node
            while head:
                head.left.next= head.right
                # Connect the children with the same parent

                if head.next:
                    head.right.next= head.next.left
                head=head.next
                # Move the head at the current level which we are traversing

            curr_node=curr_node.left
            # Move at the next level of the binary tree

        return root
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        queue=deque()
        queue.append(root)
        while queue:
            size= len(queue)
            for i in range(size):
                node=queue.popleft()
                # Means the nodes we are connecting to are of our level only
                # After the last node the next level nodes start and if we connect the right pointer to that node that is wrong
                if i<size-1 and queue:
                    node.next=queue[0]
                else:
                    node.next=None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
            