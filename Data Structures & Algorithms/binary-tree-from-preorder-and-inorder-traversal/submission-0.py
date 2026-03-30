# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        

        def helper(inorder, start, end, preorder, preorderIndex):
            if start > end:
                return None
            i = start
            while i <= end:
                if inorder[i] == preorder[preorderIndex]:
                    break
                i += 1

            
            node = TreeNode(preorder[preorderIndex])
            node.left = helper(inorder, start, i-1, preorder, preorderIndex+1)
            node.right = helper(inorder, i+1, end, preorder, preorderIndex + i-start+1)
        
            return node


        
        return helper(inorder, 0, len(inorder)-1, preorder, 0)

