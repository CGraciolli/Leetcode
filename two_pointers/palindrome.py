##https://leetcode.com/problems/valid-palindrome/

def prep(s):
    s = s.lower()
    alphanumeric = "0123456789abcdefghijklmnopqrstuvwxyz"
    S = ""
    for letter in s:
        if letter in alphanumeric:
            S += letter
    return S
    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = prep(s)
        if len(s) == 1:
            return True
        pointer1 = 0
        pointer2 = len(s) -1
        while pointer1 < pointer2:
            if s[pointer1] != s[pointer2]:
                return False
            pointer1 += 1
            pointer2 -= 1
        return True