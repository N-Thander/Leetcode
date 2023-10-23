class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n >= 4:
            while (n%4 == 0):
                n = n/4
            if n == 1:
                return 1
            else:
                return 0
        else:
            return 0
            
