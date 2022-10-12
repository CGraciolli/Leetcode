##https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s: str) -> int:
        max_length = 0
        substring = ""
        for elem in s:
            if elem not in substring:
                substring += elem
            else:
                max_length = max(max_length, len(substring))
                index = substring.index(elem)
                substring = substring[index+1:] + elem
        max_length = max(max_length, len(substring))
        return max_length