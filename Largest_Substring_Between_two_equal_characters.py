class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n = len(s)
        max_length = -1

        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    max_length = max(max_length, j - i -1)

        return max_length
