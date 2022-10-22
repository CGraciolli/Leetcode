##https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        list_of_lists = []
        curr = [root]
        while curr:
            values = []
            new_curr = []
            for elem in curr:
                if elem.left:
                    new_curr.append(elem.left)
                if elem.right:
                    new_curr.append(elem.right)
                values.append(elem.val)
            list_of_lists.append(values)
            curr = new_curr
        return list_of_lists