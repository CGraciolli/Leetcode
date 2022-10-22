##https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List


def searchInsert(nums, target):
        m = 0
        M = len(nums) - 1
        if target > nums[-1]:
            return (len(nums), False)
        if target < nums[0]:
            return (0, False)
        while m <= M:
            guess = (M + m)//2
            if target == nums[guess]:
                return (guess, True)
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
        return (m, nums[m] == target)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        index, is_zero = searchInsert(nums, 0)
        sorted_squares = []
        if is_zero == True:
            sorted_squares.append(0)
            negative = index -1
            positive = index + 1
        else:
            negative = index -1
            positive = index
        while negative >= 0 and positive < len(nums):
            if nums[negative]**2 < nums[positive]**2:
                sorted_squares.append(nums[negative]**2)
                negative -= 1
            else:
                sorted_squares.append(nums[positive]**2)
                positive += 1
        if negative >= 0:
            while negative >= 0:
                sorted_squares.append(nums[negative]**2)
                negative -= 1
        if positive < len(nums):
            while positive < len(nums):
                sorted_squares.append(nums[positive]**2)
                positive += 1
        return sorted_squares