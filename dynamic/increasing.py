##https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis_up_to = {nums[0]:1}
        for i in range(1, len(nums)):
            keys_smaller = filter(lambda x: x < nums[i], nums[0:i])
            maximum_up_to = 0
            for key in keys_smaller:
                if lis_up_to[key] > maximum_up_to:
                    maximum_up_to = lis_up_to[key]
            lis_up_to[nums[i]] = maximum_up_to + 1
        return max(list(lis_up_to.values()))