class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)

        consistent_set = 0

        for word in words:
            if all(char in allowed_set for char in word):
                consistent_set += 1


        return consistent_set 
