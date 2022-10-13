##https://leetcode.com/problems/happy-number/

def sum_sq_dig(self, n):
        n = str(n)
        soma = 0
        for i in range (len(n)):
            m = int(n[i])
            soma += m**2
        return soma

def isHappy(n):
        """
        :type n: int
        :rtype: bool
        """
        cycle = set()
        while True:
            n = sum_sq_dig(n)
            if n == 1:
                return True
            else:
                if n in cycle:
                    return False
                else:
                    cycle.add(n)