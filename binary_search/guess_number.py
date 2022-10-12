##https://leetcode.com/problems/guess-number-higher-or-lower/

##We are playing the Guess Game. The game is as follows:
##I pick a number from 1 to n. You have to guess which number I picked.
##Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
##You call a pre-defined API int guess(int num), which returns three possible results:
##-1: Your guess is higher than the number I picked (i.e. num > pick).
##1: Your guess is lower than the number I picked (i.e. num < pick).
##0: your guess is equal to the number I picked (i.e. num == pick).
##Return the number that I picked.

def guessNumber(n: int) -> int:
        m = 1
        M = n
        while True:
            pick = (m + M)//2
            if guess(pick) == 0:
                return pick
            if guess(pick) == -1:
                if M != pick:
                    M = pick
                else:
                    M -= 1
            if guess(pick) == 1:
                if m != pick:
                    m = pick
                else:
                    m += 1