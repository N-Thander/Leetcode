class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_lst = []
        odd_lst = []

        for i in nums:
            if i%2 == 0:
                even_lst.append(i)
            else:
                odd_lst.append(i)

        for j in odd_lst:
            even_lst.append(j)

        return even_lst


        
