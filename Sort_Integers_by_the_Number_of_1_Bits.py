class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def count_ones(num):
            return bin(num).count('1')

        def custom_key(num):
            return (count_ones(num), num)

        def sortByBits(arr):
            return sorted(arr, key=custom_key)

        sorted_arr = sortByBits(arr)
        return sorted_arr
