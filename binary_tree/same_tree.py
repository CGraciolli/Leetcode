##https://leetcode.com/problems/same-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def sameLeaf(leaf1, leaf2):
    if leaf1.val != leaf2.val:
        return False
    if not leaf1.right and leaf2.right:
        return False
    if leaf1.right and not leaf2.right:
        return False
    if not leaf1.left and leaf2.left:
        return False
    if leaf1.left and not leaf2.left:
        return False
    return True

def same_branch(branch1, branch2):
    if branch1 == [] and branch2 == []:
        return True
    if len(branch1) != len(branch2):
        return False
    for i in range(len(branch1)):
        if not sameLeaf(branch1[i], branch2[i]):
            return False
    return True    

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p:
            return not q
        if not q:
            return False
        curr1 = [p]
        curr2 = [q]
        while same_branch(curr1, curr2) and curr1 != []:
            new_curr1 = []
            new_curr2 = []
            for elem in curr1:
                if elem.right:
                    new_curr1.append(elem.right)
                if elem.left:
                    new_curr1.append(elem.left)
            curr1 = new_curr1
            for elem in curr2:
                if elem.right:
                    new_curr2.append(elem.right)
                if elem.left:
                    new_curr2.append(elem.left)
            curr2 = new_curr2
        return same_branch(curr1, curr2)