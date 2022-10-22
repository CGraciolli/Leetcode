##https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = len(nums) - 1
        while pointer1 < pointer2:
            go_on = True
            while go_on:
                if nums[pointer1] + nums[pointer2] == target:
                    return [pointer1 + 1, pointer2 + 1]
                if nums[pointer1] + nums[pointer2] > target:
                    pointer2 -= 1
                else:
                    pointer1 += 1
                    go_on = False