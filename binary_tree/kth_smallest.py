##https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def update_k_smallest(lista, val, k):
    """
    recives a list ordered in decreasing order and a number
    adds the element in the appropriate place in the list
    if the list has more than k elements, removes the first
    """
    if lista == []:
        return [val]
    if val >= lista[0]:
        lista = [val] + lista
    elif val <= lista[-1]:
        lista.append(val)
    else:
        M = 0
        m = len(lista) -1
        while M < m:
            if lista[M] > val:
                M += 1
            if lista[m] < val:
                m -= 1
        if val >= lista[m]:
            lista.insert(m, val)
        if val < lista[m]:
            lista.insert(m+1, val)
    if len(lista) > k:
        lista = lista[1:]
    return lista

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        k_smallest_values = [root.val]
        curr = [root]
        while curr:
            new_curr = []
            for elem in curr:
                if elem.left:
                    new_curr.append(elem.left)
                    k_smallest_values = update_k_smallest(k_smallest_values, elem.left.val, k)
                if elem.right:
                    new_curr.append(elem.right)
                    k_smallest_values = update_k_smallest(k_smallest_values, elem.right.val, k)
            curr = new_curr
        return k_smallest_values[0]