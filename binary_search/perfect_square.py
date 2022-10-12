##https://leetcode.com/problems/valid-perfect-square/
##Given a positive integer num, write a function which returns True if num is a perfect square else False.

def isPerfectSquare(num: int) -> bool:
        m = 1
        M = num//2 + 1
        if m**2 == num:
            return True
        while m <= M:
            guess = (M+m)//2
            if num > guess**2:
                if m!= guess:
                    m = guess
                else:
                    m += 1
            elif num < guess**2:
                if M != guess:
                    M = guess
                else:
                    M -= 1
            else:
                return True
        return False