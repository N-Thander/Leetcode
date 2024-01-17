from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        my_dict = Counter(arr)
        values = list(my_dict.values())

        return len(values) == len(set(values))
