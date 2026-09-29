# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        issub = False
        def serialize(node): #we want to have a function which puts it into a list
            if not node:
                return None
            return(node.val,serialize(node.left),serialize(node.right))
        subR = serialize(subRoot)
        #now we validate across the whole root TreeNode
        def validate(node):
            nonlocal issub
            if not node:
                return None
            ref = (node.val,validate(node.left),validate(node.right))
            if ref == subR:
                issub = True
            return ref
        validate(root)
        return issub