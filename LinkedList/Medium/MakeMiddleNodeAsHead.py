
from LinkedList.Easy.MergeSortedLinkedList import ListNode


def move_middle_to_head(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    prev = None  
    def find_middle(head):
        global prev
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return slow

    middle_node = find_middle(head)
    prev.next = middle_node.next
    middle_node.next = head
    head = middle_node
    return head