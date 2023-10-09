class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def binary_search_right(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        leftmost = binary_search_left(nums, target)
        rightmost = binary_search_right(nums, target)
        
        if leftmost <= rightmost:
            return [leftmost, rightmost]
        else:
            return [-1, -1]
