##https://leetcode.com/problems/top-k-frequent-elements/

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for elem in nums:
            if elem in dic.keys():
                dic[elem] += 1
            else:
                dic[elem] = 1
        list_keys = list(dic.keys())
        list_keys.sort(key= lambda x: dic[x])
        list_keys.reverse()
        return list_keys[:k]