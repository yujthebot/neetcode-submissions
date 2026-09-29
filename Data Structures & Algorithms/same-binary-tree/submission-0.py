# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return None
            L = check(node.left)
            R = check(node.right)
            return (node.val,L,R)
        if check(p)==check(q):
            return True
        else:
            return False