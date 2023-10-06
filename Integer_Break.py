class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        num_threes = n//3

        if n % 3 == 1:
            num_threes -= 1

        num_twos = (n - 3 * num_threes) // 2

        return (3 ** num_threes) * (2 ** num_twos)
