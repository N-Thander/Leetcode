class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal_triangle = {}
        for i in range(rowIndex + 1):
            row = [1] * (i+1)
            for j in range(1, i):
                row[j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]
            pascal_triangle[i] = row

        return list(pascal_triangle[rowIndex])
        
