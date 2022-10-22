##https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        first1 = list1
        first2 = list2
        if first1.val < first2.val:
            head = first1
            first1 = first1.next
        else:
            head = first2
            first2 = first2.next
        curr = head
        while first1 and first2:
            if first1.val < first2.val:
                curr.next = first1
                first1 = first1.next
            else:
                curr.next = first2
                first2 = first2.next
            curr = curr.next
        if first1:
            curr.next = first1
        if first2:
            curr.next = first2
        return head

        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return None
        if len(lists) == 1:
            return lists[0]
        merged_list = lists[0]
        for i in range(1, len(lists)):
            merged_list = mergeTwoLists(merged_list, lists[i])
        return merged_list