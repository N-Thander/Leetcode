class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def count_vowels(string):
            vowels = set("aeiouAEIOU")
            count = 0
            for char in string:
                if char in vowels:
                    count += 1

            return count

        mid = len(s)//2
        a = s[:mid]
        b = s[mid:]

        return count_vowels(a) == count_vowels(b)
