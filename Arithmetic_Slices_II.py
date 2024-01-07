class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        dp = [{} for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp_i_diff = dp[i].get(diff, 0)
                dp_j_diff = dp[j].get(diff, 0)

                count += dp_j_diff

                dp[i][diff] = dp_i_diff + dp_j_diff + 1

        return count
