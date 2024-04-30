class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0] * 1024
        count[0] = 1

        result = odd_count = 0
        mask = 0

        for char in word:
            idx = ord(char) - ord('a')
            mask ^= 1 << idx

            result += count[mask]

            for i in range(10):
                result += count[mask ^ (1 << i)]

            count[mask] += 1

        return result
