##https://leetcode.com/problems/find-the-duplicate-number/

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ##we start at the last element
        ##if we are at "value" k, "next" takes us to list[k]
        pos = nums[-1]
        U = nums[pos-1]
        pos = U
        if nums[U-1] == U:
            return U
        while True:
            for i in range(2):
                U = nums[U-1]
                if U == pos and i == 0:
                    return U
                if U == pos and i == 1:
                    pointer1 = nums[-1]
                    pointer2 = nums[pos -1]
                    while pointer1 != pointer2:
                        pointer1 = nums[pointer1 -1]
                        pointer2 = nums[pointer2 -1]
                    return pointer1
            pos = nums[pos-1]
