class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    if not head:
        return head

    prev = None
    curr = head

    while curr:
        forward = curr.next
        curr.next = prev
        prev = curr
        curr = forward

    return prev
