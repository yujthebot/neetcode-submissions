# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#attempt top down version of the structure
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validity(leftbound,node,rightbound):
            if not node:
                return True
            if not(leftbound<node.val<rightbound):
                return False
            return validity(leftbound,node.left,node.val) and validity(node.val,node.right,rightbound)
        return validity(float("-inf"),root,float("inf"))