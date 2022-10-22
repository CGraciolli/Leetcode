##https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        k = 3
        ways_minus_2 = 1 ##number of distinct ways to climb up to k-2
        ways_minus_1 = 2 ##number of distinct ways to climb up to k-1
        while k <= n:
            ways = ways_minus_1 + ways_minus_2
            ways_minus_1, ways_minus_2 = ways, ways_minus_1
            k += 1
        return ways