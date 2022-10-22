##https://leetcode.com/problems/add-two-numbers/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def soma(*digits):
    """
    recives two integers between 0 and 9
    returns a tuple (sum_digit, carry over)
    """
    soma = sum(digits)
    sum_digit = soma % 10
    carry_over = soma // 10
    return (sum_digit, carry_over)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ##easiest case: both numbers have the same number of digits
        d1 = l1
        d2 = l2
        result_sum = soma(d1.val, d2.val)
        head = ListNode(result_sum[0])
        curr = head
        while d1.next and d2.next:
            d1 = d1.next
            d2 = d2.next
            result_sum = soma(d1.val, d2.val, result_sum[1])
            new = ListNode(result_sum[0])
            curr.next = new
            curr = new
        while d1.next or d2.next:
            if d1.next:
                d1 = d1.next
                result_sum = soma(d1.val, result_sum[1])
            if d2.next:
                d2 = d2.next
                result_sum = soma(d2.val, result_sum[1])
            new = ListNode(result_sum[0])
            curr.next = new
            curr = new
        ##at this point d1.next and d2.next are None
        if result_sum[1]:
            new = ListNode(result_sum[1])
            curr.next = new
        return head