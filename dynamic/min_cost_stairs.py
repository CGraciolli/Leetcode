##https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ##starting with size 2, we save the lower cost stepping on the last step and the lowest cost not stepping on the last step (that is, stepping on the second to last step)
        pointer = 2
        last_step = cost[1]
        not_last_step = cost[0]
        while pointer < len(cost):
            temp = last_step
            last_step = cost[pointer] + min(last_step, not_last_step)
            not_last_step = temp
            pointer +=1
        return min(last_step, not_last_step)