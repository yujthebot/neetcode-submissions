# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def replace(node):
            if not node:
                return None
            l = node.left
            r = node.right
            node.right = l
            node.left = r
            replace(node.left)
            replace(node.right)
        replace(root)
        return root