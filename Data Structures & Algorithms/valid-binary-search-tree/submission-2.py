# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        BST = True
        def validation(node):
            nonlocal BST
            if not node:
                return float("inf"), float("-inf")
            leftmin, leftmax = validation(node.left)
            rightmin,rightmax = validation(node.right)
            if leftmax<node.val<rightmin:
                pass
            else:
                BST = False
            return min(node.val,rightmin,leftmin),max(node.val,leftmax,rightmax)
        validation(root)
        return BST