####https://leetcode.com/problems/search-insert-position/

from typing import List


def searchInsert(nums: List[int], target: int) -> int:
        m = 0
        M = len(nums) - 1
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        while m <= M:
            guess = (M + m)//2
            if target == nums[guess]:
                return guess
            if target > nums[guess]:
                if m != guess:
                    m = guess
                else:
                    m += 1
            if target < nums[guess]:
                if M != guess:
                    M = guess
                else:
                    M -= 1
        return m