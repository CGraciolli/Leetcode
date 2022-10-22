##https://leetcode.com/problems/number-of-1-bits/


class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n&(n-1) == 0:
            return 1
        else:
            m = n&(n-1)
            val = self.hammingWeight(m) + 1
            return val

