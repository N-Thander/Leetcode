class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_count = {}

        for word in words:
            for char in word:
                char_count[char] = char_count.get(char, 0) + 1

        num_words = len(words)
        return all(count % num_words == 0 for count in char_count.values())
