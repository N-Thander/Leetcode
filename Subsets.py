class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        powerSet = []
        def dfs(idx, subset):
            powerSet.append(subset.copy())

            for i in range(idx, n):
                subset.append(nums[i])
                dfs(i+ 1, subset)
                subset.pop()

        dfs(0, [])
        return powerSet
