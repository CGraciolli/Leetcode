##https://leetcode.com/problems/permutation-in-string/

def checkInclusion(s1: str, s2: str) -> bool:
        L = len(s1)
        ##first we create a dictionary of frequencies for the letters in s1
        d1 = {}
        for elem in s1:
            if elem in d1:
                d1[elem] += 1
            else:
                d1[elem] = 1
        ##we start our substring as the L first elements of s2
        substring = s2[:L]
        ##then we create a dictionary of frequencies for the substring
        d2 = {}
        for elem in substring:
            if elem in d2:
                d2[elem] += 1
            else:
                d2[elem] = 1
        ##then we check if s1 is a permutation of the substring
        if d1 == d2:
            return True
        for elem in s2[L:]:
            ##first we change the substring
            removed = substring[0]
            substring = substring[1:] + elem
            ##the we update it´s dictionary
            if elem in d2:
                d2[elem] += 1
            else:
                d2[elem] = 1
            d2[removed] -= 1
            if d2[removed] == 0:
                d2.pop(removed)
            if d1 == d2:
                return True
        return False