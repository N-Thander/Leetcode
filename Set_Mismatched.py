class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        dup, missing = -1, -1

        for num in nums:
            if num in seen:
                dup = num
            seen.add(num)

        for i in range(1, len(nums) + 1):
            if i not in seen:
                missing = i
                break

        return [dup, missing]
