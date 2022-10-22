##https://leetcode.com/problems/diameter-of-binary-tree/

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = 0
        curr = [root]
        while curr:
            new_curr = []
            for elem in curr:
                diam = maxDepth(elem.left) + maxDepth(elem.right)
                max_diam = max(diam, max_diam)
                if elem.right:
                    new_curr.append(elem.right)
                if elem.left:
                    new_curr.append(elem.left)
            curr = new_curr
        return max_diam