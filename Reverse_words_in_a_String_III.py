class Solution:
    def reverseWords(self, s: str) -> str:
        split_lst = s.split()
        rev_lst = []
        for i in split_lst:
            temp = i[::-1]
            rev_lst.append(temp)

        return ' '.join(rev_lst)
