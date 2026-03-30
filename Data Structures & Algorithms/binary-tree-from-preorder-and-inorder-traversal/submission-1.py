# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        seen = {}
        for idx, val in enumerate(inorder):
            seen[val] = idx
            
        def helper(start, end, preorderIndex):
            nonlocal seen
            if start > end:
                return None
            i = seen[preorder[preorderIndex]]
            node = TreeNode(preorder[preorderIndex])
            node.left = helper(start, i - 1, preorderIndex + 1)
            node.right = helper(i+1, end, preorderIndex + i - start + 1)
            return node
        
        return helper(0, len(inorder)-1, 0)

