# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        def traverse_tree(root, node_counts):
            if root is None:
                return 0
            
            traverse_tree(root.left, node_counts)

            if root.val in node_counts:
                node_counts[root.val] += 1
            else:
                node_counts[root.val] = 1

            traverse_tree(root.right, node_counts)

        node_counts = {}
        traverse_tree(root, node_counts)

        max_count = max(node_counts.values())
        max_nodes = [k for k, v in node_counts.items() if v == max_count]

        return max_nodes
        
