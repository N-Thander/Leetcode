class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_dict = {}

        for i in nums:
            freq_dict[i] = freq_dict.get(i, 0) + 1

        max_key = max(freq_dict, key=freq_dict.get)
        return max_key
