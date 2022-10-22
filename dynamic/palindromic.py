##https://leetcode.com/problems/palindromic-substrings/

def is_pal(s):
    r = s[::-1]
    return r == s

def is_within_range(s, j):
    if j >= 0:
        return j < len(s)
    return False

def howManyEvenPalCen(s, center_index):
    contador = 0
    i = 0
    go_on = True
    while i <= center_index and is_within_range(s, center_index + i + 1) and go_on:
        if is_pal(s[center_index - i : center_index + i + 2]):
            contador += 1
            i += 1
        else:
            go_on = False
    return contador

def howManyOddPalCen(s, center_index):
    contador = 0
    i = 0
    go_on = True
    while i <= center_index and is_within_range(s, center_index + i) and go_on:
        if is_pal(s[center_index - i : center_index + i + 1]):
            contador += 1
            i += 1
        else:
            go_on = False
    return contador

def howManyPalCen(s, center_index):
    return howManyOddPalCen(s, center_index) + howManyEvenPalCen(s, center_index)



class Solution:
    def countSubstrings(self, s: str) -> int:
        contador = 0
        for i in range(len(s)):
            contador += howManyPalCen(s, i)
        return contador
        