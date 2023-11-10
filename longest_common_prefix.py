class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()

        first_str, last_str = strs[0], strs[-1]

        common_prefix = []

        for i, char in enumerate(first_str):
            if i < len(last_str) and last_str[i] == char:
                common_prefix.append(char)
            else:
                break

        return "".join(common_prefix)
