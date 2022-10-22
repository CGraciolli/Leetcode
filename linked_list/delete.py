##https://leetcode.com/problems/delete-node-in-a-linked-list/

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        one_after = node.next
        two_after = one_after.next
        node.next = two_after
        node.val = one_after.val