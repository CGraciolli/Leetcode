##https://leetcode.com/problems/longest-palindromic-substring/

def is_pal(s):
        r = s[::-1]
        return r == s

def is_within_range(s, j):
        if j >= 0:
            return j < len(s)
        return False

def longestEvenPalCen(s, center_index, min_size):
    i = min_size//2
    go_on = True
    longest_pal = s[center_index]
    while i <= center_index and is_within_range(s, center_index + i + 1) and go_on:
        if is_pal(s[center_index - i : center_index + i + 2]):
            longest_pal = (s[center_index - i : center_index + i + 2])
            i += 1
        else:
            go_on = False
    return longest_pal

def longestOddPalCen(s, center_index, min_size):
    i = min_size//2
    go_on = True
    longest_pal = s[center_index]
    while i <= center_index and is_within_range(s, center_index + i) and go_on:
        if is_pal(s[center_index - i : center_index + i + 1]):
            longest_pal = (s[center_index - i : center_index + i + 1])
            i += 1
        else:
            go_on = False
    return longest_pal
            
    

def longestPalCen(s, center_index, min_size):
    if len(longestEvenPalCen(s, center_index, min_size)) > len(longestOddPalCen(s, center_index, min_size)):
        return longestEvenPalCen(s, center_index, min_size)
    return longestOddPalCen(s, center_index, min_size)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        long_pal = ""
        for center_index in range(len(s)):
            if len(longestPalCen(s, center_index, len(long_pal))) > len(long_pal):
                long_pal = longestPalCen(s, center_index, len(long_pal))
        return long_pal