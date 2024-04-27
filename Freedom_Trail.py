class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def min_distance(start, end):
            return min(abs(start - end), len(ring) - abs(start - end))

        memo = {}

        def dp(index, ring_index):
            if index == len(key):
                return 0
            if (index, ring_index) in memo:
                return memo[(index, ring_index)]

            char = key[index]
            min_steps = float('inf')
            for i, c in enumerate(ring):
                if c == char:
                    steps_to_align = min_distance(ring_index, i)
                    steps_to_press = 1
                    total_steps = steps_to_align + steps_to_press
                    next_index = dp(index + 1, i)
                    min_steps = min(min_steps, total_steps + next_index)

            memo[(index, ring_index)] = min_steps
            return min_steps

        return dp(0, 0)
