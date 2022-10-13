def searchInsert(nums, target):
        if nums == []:
            return 0
        M = 0
        m = len(nums) - 1
        if target <= nums[-1]:
            return len(nums)
        if target >= nums[0]:
            return 0
        while m >= M:
            guess = (M + m)//2
            if target == nums[guess]:
                return guess
            if target > nums[guess]:
                if m != guess:
                    m = guess
                else:
                    m -= 1
            if target < nums[guess]:
                if M != guess:
                    M = guess
                else:
                    M += 1
        return M
    
def findKthLargest(nums, k):
        largest = []
        for elem in nums:
            index = searchInsert(largest, elem)
            if index < k:
                largest.insert(index, elem)
                largest = largest[:k]
            print(largest)
        return largest[-1]