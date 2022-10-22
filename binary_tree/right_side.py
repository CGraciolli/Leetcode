##https://leetcode.com/problems/binary-tree-right-side-view/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        R = []
        curr = [root]
        while curr:
            new_curr = []
            for elem in curr:
                if elem.left:
                    new_curr.append(elem.left)
                if elem.right:
                    new_curr.append(elem.right)
            R.append(curr[-1].val)
            curr = new_curr
        return R