from LinkedList.Easy.MergeSortedLinkedList import ListNode


def sort_list(head: ListNode) -> ListNode:
    def middle_node( head):
        # if head is None or head.next is None:
        #     return head
        slow=fast=head
        while fast.next and fast.next.next:
           slow=slow.next
           fast=fast.next.next
        return slow

    def merge_sorted_linked_list(head1, head2):
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
        if p2:
            curr.next = p2
        return dummy_head.next
    
    
    
    if head is None or head.next is None:
            return head
        # get the middle of linked list
    middle = middle_node(head)
    nextToMiddle = middle.next
    
    # so that one linked list is divided into 2 parts
    middle.next = None
    
    # apply merge sort on left & right sub-list
    left = sort_list(head)
    right = sort_list(nextToMiddle)
    
    # merge the sorted left and right sub-lists
    sortedList=merge_sorted_linked_list(left, right)
    
    return sortedList

    