##https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        dic_val = {preorder[0]: root} ##connects value to nodes
        ##list that relates the indexes of preorder and inorder
        pre_inorder = []
        for elem in preorder:
            pre_inorder.append(inorder.index(elem))
        for i, elem in enumerate(preorder):
            if (i+1) < len(preorder):
                after = TreeNode(preorder[i+1]) ##next element in the preorder
                dic_val[after.val] = after
                ##if after comes before elem in the inorder, elem.left = after
                if pre_inorder[i] > pre_inorder[i+1]:
                    dic_val[elem].left = after
                ##HERE LIES THE PROBLEM
                else:
                    ##index of after in inorder
                    j = pre_inorder[i+1]
                    k = j - 1
                    go_on = True
                    while go_on and k >= 0:
                        if inorder[k] in dic_val:
                            dic_val[inorder[k]].right = after
                            go_on = False
                        k -= 1
        return root
