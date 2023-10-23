class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n >= 3:
            while (n%3 == 0):
                n = n/3
            if n == 1:
                return 1
            else:
                return 0
        else:
            return 0
