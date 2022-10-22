##https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        return self.look_for_tens(digits)
    
    def look_for_tens(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) -1, 0, -1):
            if digits[i] == 10:
                digits[i] = 0
                digits[i -1] += 1
        if digits[0] == 10:
            digits = [1, 0] + digits[1:]
        return digits
        