##https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ##keys are the position on the list, the values, the nodes
        dict_storage = {1: head}
        curr = head
        pos = 1
        while curr.next:
            pos += 1
            curr = curr.next
            dict_storage[pos] = curr
        ##at this point pos should b len(list)
        ##r is the position of the node to be removed
        r = pos - n + 1
        ##if there is only one node
        if not head.next:
            return None
        ##general case, there are more than one node, we are not removing the head or the tail
        if r-1 in dict_storage and r+1 in dict_storage:
            before = dict_storage[r-1]
            after = dict_storage[r+1]
            before.next = after
            return head
        ##there are more than one node and we are removing the tail
        if not r+1 in dict_storage:
            before = dict_storage[r-1]
            before.next = None
            return head
        #there are more than one node and we are removing the head
        if not r-1 in dict_storage:
            return dict_storage[r+1]