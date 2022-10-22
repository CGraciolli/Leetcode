##https://leetcode.com/problems/house-robber/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        ##maximum amount of money robbing houses until number n, not robbing n
        max_money_1 = nums[0]
        ####maximum amount of money robbing houses until number n,t robbing n
        max_money_2 = nums[1]
        for i in range(2, len(nums)):
            new_max_money_2 = max(max_money_1, max_money_2 - nums[i-1]) + nums[i]
            max_money_1, max_money_2 = max_money_2, new_max_money_2
        return max(max_money_1, max_money_2)