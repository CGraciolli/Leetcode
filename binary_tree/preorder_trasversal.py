##https://leetcode.com/problems/binary-tree-preorder-traversal/

from collections import deque

def preorder(node):
    """
    assumes node is not None
    """
    preorder = deque([node.val])
    if node.left != None:
        preorder.append(node.left)
    if node.right != None:
        preorder.append(node.right)
    return preorder

def preorderTraversal(root):
    if root == None:
        return []
    preorder_list = preorder(root)
    ##we should apply the preorder function to every item of the preorder_list that is a TreeNode
    ##and then put the result in the place where the TreeNode used to be on the preorder_list
    ##when the preorderlist has only integers (no TreeNodes) we can stop the loop
    last = []
    while len(last) != len(preorder_list): ##change to something like while there are TreeNodes in the list
        new_preorder_list = []
        for elem in preorder_list:
            if isinstance(elem, TreeNode):
                new_preorder_list += preorder(elem)
            else:
                new_preorder_list.append(elem)
        last = preorder_list
        preorder_list = new_preorder_list
    return preorder_list