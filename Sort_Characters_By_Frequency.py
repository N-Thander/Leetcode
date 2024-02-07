class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        sorted_chars =  sorted(char_count, key=lambda x: char_count[x], reverse= True)
        sorted_string = ''.join(char*char_count[char] for char in sorted_chars)

        return sorted_string

    
