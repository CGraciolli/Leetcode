##https://leetcode.com/problems/search-a-2d-matrix/

def binarySearch(nums:list[int], target:int) -> int:
        M = len(nums) -1
        m = 0
        if target > nums[M]:
            return False
        if target < nums[m]:
            return False
        while m <= M:
            guess = (M + m)//2
            if nums[guess] == target:
                return True
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
        return False

def searchInsert(nums: list[int], target: int) -> int:
        m = 0
        M = len(nums) - 1
        if target > nums[-1]:
            return len(nums), False
        if target < nums[0]:
            return 0, False
        while m <= M:
            guess = (M + m)//2
            if target == nums[guess]:
                return guess, True
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
        return m, False

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
        ##frist we use searchInsert to determine the right row
        firsts = []
        for row in matrix:
            firsts.append(row[0])
        R, is_in_row = searchInsert(firsts, target)
        ##if we find the target in the first element of one of the rows, we return True
        if is_in_row:
            return True
        ##otherwise, we need to search for the target on the row number R - 1
        else:
            row = R - 1
            return binarySearch(matrix[row], target)