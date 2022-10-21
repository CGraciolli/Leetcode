#https://leetcode.com/problems/binary-tree-postorder-traversal/

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def postorder(root):
    postorder = deque([root.val])
    if root.right != None:
        postorder.appendleft(root.right)
    if root.left != None:
        postorder.appendleft(root.left)
    return postorder

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        postorder_list = postorder(root)
        last = []
        while last != postorder_list:
            new_postorder_list = []
            for elem in postorder_list:
                if isinstance(elem, TreeNode):
                    new_postorder_list += postorder(elem)
                else:
                    new_postorder_list.append(elem)
            last = postorder_list
            postorder_list = new_postorder_list
        return postorder_list