##https://leetcode.com/problems/counting-bits/


from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        k = 1
        while k <= n:
            if k&(k-1) == 0: ##k is a 1 followed by 0s
                ans.append(1)
            elif k&(k-1) == k-1: ##k has a 1 as the last digit
                last_val = ans[-1]
                ans.append(last_val + 1)
            else:
                intersection = k&(k-1)
                ans.append(ans[intersection] + 1)
            k += 1
        return ans

