##https://leetcode.com/problems/binary-search/


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        M = len(nums) -1
        m = 0
        if target > nums[M]:
            return -1
        if target < nums[m]:
            return -1
        while m <= M:
            guess = (M + m)//2
            if nums[guess] == target:
                return guess
            if nums[guess] > target:
                if guess != M:
                    M = guess
                else:
                    M -= 1
            if nums[guess] < target:
                if guess != m:
                    m = guess
                else:
                    m += 1
        return -1