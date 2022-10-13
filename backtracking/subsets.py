def rotate(lista , k):
    return lista[k:] + lista[:k]

def subsets(nums):
        subsets = [nums, []]
        for k in range(len(nums)):
            rotated = rotate(nums, k)
            print(rotated)
            for i in range(1, len(nums)):
                rotated = rotated[1:]
                subsets.append(rotated)
        return subsets