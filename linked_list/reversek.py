##https://leetcode.com/problems/reverse-nodes-in-k-group/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKNodes(head, k):
    """
    recives a head of a list with at least k nodes
    reverses the first k
    return a tuple (head, tail)
    """
    ##if it is empty
    if not head:
        return head
    before = head
    curr = head.next
    ##the head of the original list won't have a next in the reversed list
    head.next = None
    for _ in range(k-1):
        temp = curr.next
        curr.next = before
        before = curr
        curr = temp
    return (before, head)

def checkN(head, k):
    """
    checks if there is k -1 elements after head
    return a tuple, the first element being a boolean
    and the second the next after k (may be None)
    """
    curr = head
    for _ in range(k-1):
        if not curr.next:
            return (False, None)
        curr = curr.next
    return (True, curr.next)
    
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ##checks if the list is empty
        if not head:
            return None
        ##checks if there are at least k elements
        are_there_k, after = checkN(head, k)
        if not are_there_k:
            return head
        ##if k is 1, nothing changes
        if k == 1:
            return head
        ##if we are here, there are at least k elements
        ##we change the "head" to the (k+1)th element
        next_head = after
        ##the head is the k element
        ##the "tail" is the old head (we will use the "tail" in order to join the k-length lists) 
        head, tail = reverseKNodes(head, k)
        ##the "tail" is joined to the rest of the list
        tail.next = after
        ##checks if the list doesn´t end after the k cluster
        while after:
            curr = after
            are_there_k, after = checkN(curr, k)
            ##if there are not at least k more elements, we stop (after will be None)
            if are_there_k:
                next_head, new_tail = reverseKNodes(next_head, k)
                ##we change how the lists are concatenated
                tail.next = next_head
                ##we concatenate the end of the k-length cluster to the rest of the list
                new_tail.next = after
                ##we change the "head" for the new k-length cluster
                next_head = after
                ##we change the tail of hte k-
                tail = new_tail
        return head