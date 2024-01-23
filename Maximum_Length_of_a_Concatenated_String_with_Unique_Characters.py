class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique(sub):
            return len(sub) == len(set(sub))
        
        def backtrack(start, path):
            nonlocal max_len
            
            max_len = max(max_len, len(path))

            for i in range(start, len(arr)):
                if is_unique(path + arr[i]):
                    backtrack(i + 1, path + arr[i])

        max_len = 0
        backtrack(0, "")
        return max_len

    
