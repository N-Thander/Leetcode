class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev1, prev2 = 0, 0

        for i in range(2, n + 1):
            curr = min(prev1 + cost[i-1], prev2 + cost[i - 2])
            prev1, prev2 = curr, prev1

        return prev1
