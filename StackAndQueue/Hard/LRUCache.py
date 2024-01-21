from collections import defaultdict

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = defaultdict(ListNode)
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        node = self.hash_map[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node_to_remove = self.hash_map[key]
            self._remove(node_to_remove)

        node = ListNode(key, value)
        self.hash_map[key] = node
        self._add(node)

        if len(self.hash_map) > self.capacity:
            deletion_node = self.head.next
            self._remove(deletion_node)
            del self.hash_map[deletion_node.key]

    def _add(self, node):
        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, curr_node):
        curr_node.prev.next = curr_node.next
        curr_node.next.prev = curr_node.prev