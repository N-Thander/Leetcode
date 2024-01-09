# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_nodes_in_order(root):
            result = [] 
            if root:
                if not root.left and not root.right:
                    result.append(root.val)
                result.extend(get_leaf_nodes_in_order(root.left))
                result.extend(get_leaf_nodes_in_order(root.right))
            return result

        leaf_node_root1 = get_leaf_nodes_in_order(root1)
        leaf_node_root2 = get_leaf_nodes_in_order(root2)

        return leaf_node_root1 == leaf_node_root2
