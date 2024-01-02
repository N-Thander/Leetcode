class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result = []

        for num in nums:
            found = False
            for row in result:
                if num not in row:
                    row.append(num)
                    found = True
                    break

            if not found:
                result.append([num])

        return result
