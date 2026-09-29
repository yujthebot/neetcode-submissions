# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0
        def diameter(node):
            nonlocal best
            if not node:
                return 0
            L = diameter(node.left)
            R = diameter(node.right)
            best = max(best,L+R)
            return 1+max(L,R)
        diameter(root)
        return best
