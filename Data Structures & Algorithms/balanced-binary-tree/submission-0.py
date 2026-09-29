# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def depth(node):
            if not node:
                return (0,self.balanced)
            L, left_balance = depth(node.left)
            R, right_balance  = depth(node.right)
            if abs(L-R) > 1 or right_balance == False or left_balance == False:
                self.balanced = False
            return (1+max(L,R), self.balanced)
        
        return depth(root)[1]

        