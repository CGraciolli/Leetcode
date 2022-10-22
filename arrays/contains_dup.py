##https://leetcode.com/problems/contains-duplicate/submissions/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        return len(nums) != len(nums_set)