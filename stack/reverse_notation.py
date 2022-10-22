##https://leetcode.com/problems/evaluate-reverse-polish-notation/

from math import ceil
from typing import List

def operation(n1, n2, operator):
    n1 = int(n1)
    n2 = int(n2)
    if operator == "+":
        return str(n1 + n2)
    if operator == "-":
        return str(n1 - n2)
    if operator == "*":
        return str(n1 * n2)
    if operator == "/" and n1*n2 >= 0:
        return str(n1 // n2)
    if operator == "/" and n1*n2 < 0:
        return str(ceil(n1/n2))
    
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        while len(tokens) > 1:
            go_on = True
            index = 0
            while go_on and index < len(tokens):
                if tokens[index] in operators:
                    result = operation(tokens[index-2], tokens[index-1], tokens[index])
                    if index == 2:
                        tokens = [result] + tokens[index+1:]
                    else:
                        tokens = tokens[:index-2] + [result] + tokens[index+1:]
                    go_on = False
                index += 1
        return int(tokens[0])