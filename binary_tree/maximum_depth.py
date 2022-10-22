##https://leetcode.com/problems/maximum-depth-of-binary-tree/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        curr = [root]
        depth = 0
        while curr:
            depth += 1
            new_curr = []
            for elem in curr:
                if elem.right:
                    new_curr.append(elem.right)
                if elem.left:
                    new_curr.append(elem.left)
            curr = new_curr
        return depth