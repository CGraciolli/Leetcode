##https://leetcode.com/problems/product-of-array-except-self/

from functools import reduce
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = reduce(lambda x, y : x*y, nums, 1)
        answer = []
        for index, num in enumerate(nums):
            if num != 0:
                answer.append(product//num)
            else:
                answer.append(reduce(lambda x, y : x*y, nums[: index] + nums[index+1:], 1))
        return answer