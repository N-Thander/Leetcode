class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.helper(nums, 0, 0)

    def helper(self, nums: List[int], index: int, currValue: int) -> int:
        if index == len(nums):
            return currValue
        return self.helper(nums, index + 1, currValue ^ nums[index]) + self.helper(nums, index + 1, currValue)
