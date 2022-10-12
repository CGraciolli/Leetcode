##https://leetcode.com/problems/time-based-key-value-store/

def searchInsert(nums, target):
        m = 0
        M = len(nums) - 1
        if target > nums[-1]:
            return (False, len(nums))
        if target < nums[0]:
            return (False, 0)
        while m <= M:
            guess = (M + m)//2
            if target == nums[guess]:
                return (True, guess)
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
        return (False, m)

class TimeMap:

    def __init__(self):
        self.keys = set()
        self.dict = {} ##the keys are the keys, the values are a tuple of lists, one with timestamps, the other with values
        
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys.add(key)
            self.dict[key] = ([timestamp], [value])
        else:
            self.dict[key][0].append(timestamp) 
            self.dict[key][1].append(value)
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        timestamps, values = self.dict[key]
        boolean, index = searchInsert(timestamps, timestamp)
        if boolean:
            return values[index]
        else:
            if index == 0:
                return ""
            else:
                return values[index-1]