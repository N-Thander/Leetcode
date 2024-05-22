class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(subs):
            return subs == subs[::-1]

        def backtrack(start, path, result):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(end, path, result)
                    path.pop()


        result = []
        backtrack(0, [], result)
        return result
