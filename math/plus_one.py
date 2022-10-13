##https://leetcode.com/problems/plus-one/

   
def look_for_tens(digits):
        for i in range(len(digits) -1, 0, -1):
            if digits[i] == 10:
                digits[i] = 0
                digits[i -1] += 1
        if digits[0] == 10:
            digits = [1, 0] + digits[1:]
        return digits

def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        return look_for_tens(digits)