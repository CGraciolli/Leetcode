##https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def convert_to_nodes(data):
    """recieves a list of values, returns a list of nodes"""
    list_nodes = []
    for elem in data:
        if elem != "":
            list_nodes.append(TreeNode(int(elem)))
        else:
            list_nodes.append(None)
    return list_nodes
                             
    
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialized = ""
        curr = [root]
        while curr != []:
            new_curr = []
            for elem in curr:
                if elem != None:
                    serialized += str(elem.val) + ","
                    new_curr.append(elem.left)
                    new_curr.append(elem.right)
                else:
                    serialized += ","
            curr = new_curr
        return serialized
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        list_data = data.split(",")
        list_nodes = convert_to_nodes(list_data)
        root = list_nodes[0]
        pointer1 = 0 ##treenode where we eant to define left and right
        pointer2 = 1 ##node tp be attached to either left or right
        while pointer2 < len(list_nodes) and pointer1 < len(list_nodes):
            if list_nodes[pointer1]!= None:
                list_nodes[pointer1].left = list_nodes[pointer2]
                list_nodes[pointer1].right = list_nodes[pointer2 + 1]
                pointer2 += 2
            pointer1 += 1 
            
        return root