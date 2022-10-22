##https://leetcode.com/problems/subtree-of-another-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def same_leaf(leaf1, leaf2):
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
        if not same_leaf(branch1[i], branch2[i]):
            return False
    return True

def same_tree(root1, root2):
    """
    is given two roots of binary trees
    returns True if the trees are identical, False otherwise
    assumes neither root is None
    """
    curr1 = [root1]
    curr2 = [root2]
    #while curr1 == curr2 and curr1 != []:
    while same_branch(curr1, curr2) and curr1 != []:
        new_curr1 = []
        new_curr2 = []
        for elem in curr1:
            if elem.left:
                new_curr1.append(elem.left)
            if elem.right:
                new_curr1.append(elem.right)
        curr1 = new_curr1
        for elem in curr2:
            if elem.left:
                new_curr2.append(elem.left)
            if elem.right:
                new_curr2.append(elem.right)
        curr2 = new_curr2
    return len(curr1) == 0

class Solution:
    ##maybe we can use tree depth in order to speed things up
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        curr = [root]
        while curr:
            new_curr = []
            for elem in curr:
                if same_tree(elem, subRoot):
                    return True
                if elem.left:
                    new_curr.append(elem.left)
                if elem.right:
                    new_curr.append(elem.right)
            curr = new_curr
        return False