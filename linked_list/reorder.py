##https://leetcode.com/problems/reorder-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dict_storage = {0:head}
        pos = 0
        curr = head
        while curr.next:
            curr = curr.next
            pos += 1
            dict_storage[pos] = curr
        ##at this point, we should heave a dictionary whose keys are the position in the list, and whose values are the respective nodes
        ##pos should be len(list)-1
        i = 0
        while i < (pos + 1)//2:
            dict_storage[i].next = dict_storage[pos-i]
            dict_storage[pos-i].next = dict_storage[i + 1]
            i += 1
        if pos % 2 == 1:
            dict_storage[i].next = None
            return head
        else:
            dict_storage[i].next = dict_storage[pos-i]
            dict_storage[pos-i].next = None
            return head