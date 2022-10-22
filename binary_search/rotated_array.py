##https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


def binarySearch(nums:List[int], target:int) -> int:
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

def search(nums: List[int], target: int) -> int:
    ##if the list has only one number
    if len(nums) == 1:
        return nums[0] == target
    ##if there is not pivot
    if nums[0] < nums[-1]:
        return binarySearch(nums, target)
    ##if there is a pivot
    m = 0
    M = len(nums) - 1
    ##first we check the extremities
    if nums[m] == target:
        return m
    if nums[M] == target:
        return M
    ##then we start the loop
    while m <= M:
        ##the guess will be in the middle of the upper bouns (M) and the lower bound(m)
        guess = (m + M)//2
        ##we check the guess
        if nums[guess] == target:
            return guess
        ##if the lower bound is smaller than guess, nums[m:guess+1] is sorted
        if nums[m] <= nums[guess]:
            ##if the target is bigger than nums[m] and smaller than nums[guess], we should look at nums[m:guess+1]
            if target >= nums[m] and target <= nums[guess]:
                if M != guess:
                    M = guess
                else:
                    M -= 1
            ##otherwise, we should look at nums[guess:M]
            else:
                if m != guess:
                    m = guess
                else:
                    m += 1
        ##if the lower bound is greater than guess, nums[guess:M] is sorted
        else:
            ##if the target is greater than guess and smaller than the upper bouns, we shoould look at nums[guess:M]
            if target >= nums[guess] and target <= nums[M]:
                if m != guess:
                    m = guess
                else:
                    m += 1
            ##otherwise, we should look at nums[0:guess]
            else:
                if M != guess:
                    M = guess
                else:
                    M -= 1
    return -1


    