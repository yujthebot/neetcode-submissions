# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def validity(node, maxval):
            nonlocal count
            if not node:
                return 0
            if node.val>=maxval:
                count+=1
            maxval = max(maxval, node.val)
        
            validity(node.left,maxval)
            validity(node.right,maxval)
        validity(root,root.val)
        return count
            
            