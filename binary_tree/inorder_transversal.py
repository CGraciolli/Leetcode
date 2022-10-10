from collections import deque

def inorder(node):
    """
    assumes node is not None
    """
    inorder = deque([node.val])
    if node.left != None:
        inorder.appendleft(node.left)
    if node.right != None:
        inorder.append(node.right)
    return inorder

def inorderTraversal(root):
    if root == None:
        return []
    inorder_list = inorder(root)
    ##we should apply the inorder function to every item of the inorder_list that is a TreeNode
    ##and then put the result in the place where the TreeNode used to be on the inorder_list
    ##when the inorder_list has only integers (no TreeNodes) we can stop the loop
    last = []
    while len(last) != len(inorder_list): ##change to something like while there are TreeNodes in the list
        new_inorder_list = []
        for elem in inorder_list:
            if isinstance(elem, TreeNode):
                new_inorder_list += inorder(elem)
            else:
                new_inorder_list.append(elem)
        last = inorder_list
        inorder_list = new_inorder_list
    return inorder_list