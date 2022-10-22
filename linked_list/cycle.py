##https://leetcode.com/problems/linked-list-cycle/

class Solution:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ##checks if the list of nodes is not empty
        if not head:
            return False
        ##checks if head ends a cycle of size 1
        if head.next == head:
            return True
        ##U is the result of applying next n times in the element of position n
        ##here n is 1
        U = head.next
        ##current_tail is the element of position n
        ##we want to determine id there is a cycle ending in current_tail
        ##said circle must be of size n or smaller
        current_tail = head.next
        ##checks if such numbers exists, if it doesn´t, we are not in a cyle
        while current_tail:
            ##checks if applying next to U once or twice gives us current_tail
            ##in which case, we are in a cycle
            for _ in range(2):
                if not U:
                    return False
                U = U.next
                if U == current_tail:
                    return True
            ##if not, we change current_tail
            current_tail = current_tail.next
        return False