import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        min_heap = []
        
        for node in lists:
            while node:
                heapq.heappush(min_heap, node.val)
                node = node.next

        result = ListNode()
        temp = result

        while min_heap:
            temp.next = ListNode(heapq.heappop(min_heap))
            temp = temp.next

        return result.next
