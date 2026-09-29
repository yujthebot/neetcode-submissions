# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        valid = False
        def serialize(node):
        
            if not node:
                return None
            L= serialize(node.left)
            R= serialize(node.right)
            
            return (node.val,L,R)
        sub = serialize(subRoot)
        def search(node):
            if not node:
                return None
            L = search(node.left)
            R = search(node.right)
            if L or R:
                return True
            elif serialize(node) == sub:
                return True
            elif serialize(node.left)==sub or serialize(node.right) == sub:
                return True
            else:
                return False
        return search(root)

        