# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        temp = root
        prev = None
        while temp:
            if temp.val > val:
                prev = temp
                temp = temp.left
            else:
                prev = temp
                temp = temp.right
        if prev and prev.val > val:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)
        
        return root