# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        p1 = head1
        p2 = head2
        dummy_head = ListNode(-1)
        curr = dummy_head

        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                curr = curr.next
                p1 = p1.next
            else:
                curr.next = p2
                curr = curr.next
                p2 = p2.next
        if p1:
            curr.next = p1
            p1 = p1.next
            curr = curr.next
        if p2:
            curr.next = p2
            p2 = p2.next
            curr = curr.next
        return dummy_head.next
        
        
        
        