##https://leetcode.com/problems/binary-tree-maximum-path-sum/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        dict_fathers = {root:None}
        dict_biggest_path = {} ##keys are nodes, values are the maximum sum of a path starting at the node and descending
        curr = [root]
        nodes = curr
        while curr != []:
            new_curr = []
            for elem in curr:
                if elem.left != None:
                    dict_fathers[elem.left] = elem
                    new_curr.append(elem.left)
                if elem.right != None:
                    dict_fathers[elem.right] = elem
                    new_curr.append(elem.right)
            nodes += new_curr
            curr = new_curr
        nodes = nodes[::-1]
        for elem in nodes:
            possibilities = [0]
            if elem.left != None:
                possibilities.append(dict_biggest_path[elem.left])
            if elem.right != None:
                possibilities.append(dict_biggest_path[elem.right])
            dict_biggest_path[elem] = elem.val + max(possibilities)
        ##list of the maximum sum paths with each node as the appex
        max_sum_path = root.val
        nodes = list(dict_fathers.keys())
        for node in nodes:
            if node.left == None and node.right == None:
                max_sum_path = max(max_sum_path, node.val)
            elif node.left == None:
                max_sum_path = max([max_sum_path, node.val + max(0,  dict_biggest_path[node.right])])
            elif node.right == None:
                max_sum_path = max([max_sum_path, node.val + max(0,  dict_biggest_path[node.left])])
            else:
                max_sum_path = max([max_sum_path, node.val + max([0,  dict_biggest_path[node.left], dict_biggest_path[node.right], dict_biggest_path[node.right] + dict_biggest_path[node.left]])])
        return max_sum_path
        