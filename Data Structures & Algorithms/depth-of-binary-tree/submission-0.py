# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        best = 0
        def depth(node):
            nonlocal best
            if not node:
                return 1
            L = depth(node.left)
            R = depth(node.right)
            best = max(best,L,R)
            return 1 + max(L,R)
        depth(root)
        return best