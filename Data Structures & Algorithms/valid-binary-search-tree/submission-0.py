# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def preorder(root, l, r):
            if not root:
                return True
            
            if not (l<root.val<r): return False

            return preorder(root.left, l, root.val) and preorder(root.right, root.val, r)
        
        return preorder(root, -math.inf, math.inf)