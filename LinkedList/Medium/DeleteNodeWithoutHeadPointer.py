from LinkedList.Easy.MergeSortedLinkedList import ListNode


def delete_given_node(head: ListNode, node: ListNode) -> ListNode:
    value= node.next.val
    node.val=value
    node.next= node.next.next
    return head
