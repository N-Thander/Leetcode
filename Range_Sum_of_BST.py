# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            
            current_sum = 0
            
            if low <= node.val <= high:
                current_sum += node.val
            
            current_sum += dfs(node.left)
            current_sum += dfs(node.right)
            
            return current_sum

        return dfs(root)
