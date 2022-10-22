##https://leetcode.com/problems/invert-binary-tree/


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def invert_node(node):
    left = node.left
    right = node.right
    node.left = right
    node.right = left
    return node
    
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        curr = [root]
        while curr:
            new_curr = []
            for elem in curr:
                invert_node(elem)
                if elem.left:
                    new_curr.append(elem.left)
                if elem.right:
                    new_curr.append(elem.right)
            curr = new_curr
        return root