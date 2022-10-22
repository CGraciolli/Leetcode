##https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List


def findMin(nums:List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        M = len(nums) - 1
        while nums[m] > nums[M]:
            guess = (m+M)//2
            if nums[guess] < nums[M]:
                if guess != M:
                    M = guess
                else:
                    M -= 1
            if nums[guess] > nums[M]:
                if guess != m:
                    m = guess
                else:
                    m += 1
            
        return nums[m]
        