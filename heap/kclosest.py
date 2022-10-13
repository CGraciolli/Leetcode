def distance(lista):
    return lista[0]**2 + lista[1]**2

def searchInsert(nums, target):
        if nums == []:
            return 0
        m = 0
        M = len(nums) - 1
        if distance(target) < distance(nums[0]):
            return 0
        if distance(target) > distance(nums[-1]):
            return len(nums)
        while m <= M:
            guess = (M + m)//2
            if distance(target) == distance(nums[guess]):
                return guess
            if distance(target) > distance(nums[guess]):
                if m != guess:
                    m = guess
                else:
                    m += 1
            if distance(target) < distance(nums[guess]):
                if M != guess:
                    M = guess
                else:
                    M -= 1
        return m

def kClosest(points, k):
        closer = []
        for point in points:
            index = searchInsert(closer, point)
            if index < k:
                closer.insert(index, point)
            print(closer)
        return closer[:k]