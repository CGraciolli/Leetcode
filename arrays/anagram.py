##https://leetcode.com/problems/valid-anagram/submissions/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_freq_s = {}
        for letter in s:
            if letter in dic_freq_s:
                dic_freq_s[letter] += 1
            else:
                dic_freq_s[letter] = 1
        dic_freq_t = {}
        for letter in t:
            if letter in dic_freq_t:
                dic_freq_t[letter] += 1
            else:
                dic_freq_t[letter] = 1
        return dic_freq_t == dic_freq_s