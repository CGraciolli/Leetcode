##https://leetcode.com/problems/count-good-nodes-in-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
        
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curr = [root]
        max_path = [root.val]
        counter = 1
        while curr:
            new_curr = []
            new_max_path = []
            for i in range(len(curr)):
                if curr[i].left:
                    new_curr.append(curr[i].left)
                    if curr[i].left.val >= max_path[i]:
                        new_max_path.append(curr[i].left.val)
                        counter += 1
                    else:
                        new_max_path.append(max_path[i])
                if curr[i].right:
                    new_curr.append(curr[i].right)
                    if curr[i].right.val >= max_path[i]:
                        new_max_path.append(curr[i].right.val)
                        counter += 1
                    else:
                        new_max_path.append(max_path[i])
            curr = new_curr
            max_path = new_max_path
        return counter