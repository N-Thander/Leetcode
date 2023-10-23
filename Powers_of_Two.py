class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n >= 2:
            while (n%2 == 0):
                n = n/2
            if n == 1:
                return 1
            else:
                return 0
        else:
            return 0
