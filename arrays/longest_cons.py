##https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ##for each element n, we check if n-1 and n+1 are on the list, and keep checking on each direction until they aren´t
        ##we keep a set of visited numbers in order to increase speed
        nums = set(nums)
        visited = set()
        longest_cons_seq = 0
        for elem in nums:
            if elem not in visited:
                cons_seq = 1
                visited.add(elem)
                i = 1
                while elem + i in nums:
                    visited.add(elem +i)
                    cons_seq += 1
                    i += 1
                j = 1
                while elem - j in nums:
                    visited.add(elem - j)
                    cons_seq += 1
                    j += 1
                longest_cons_seq = max(longest_cons_seq, cons_seq)               
        return longest_cons_seq