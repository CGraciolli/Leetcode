##https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def maxDepth(root):
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

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        curr = [root]
        while curr:
            new_curr = []
            for elem in curr:
                L = maxDepth(elem.left)
                R = maxDepth(elem.right)
                if abs(L - R) > 1:
                    return False
                if elem.left:
                    new_curr.append(elem.left)
                if elem.right:
                    new_curr.append(elem.right)
            curr = new_curr
        return True