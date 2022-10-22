##https://leetcode.com/problems/reverse-linked-list/

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ##if it is empty
        if not head:
            return head
        before = head
        curr = head.next
        ##the head of the original list won't have a next in the reversed list
        head.next = None
        while curr:
            temp = curr.next
            curr.next = before
            before = curr
            curr = temp
        return before