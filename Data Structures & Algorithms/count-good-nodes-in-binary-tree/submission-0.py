# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def preorder_path(root, max_till_now):
            nonlocal count
            if not root:
                return

            if max_till_now <= root.val:
                count += 1
                max_till_now = root.val
            preorder_path(root.left, max_till_now)
            preorder_path(root.right, max_till_now)

        preorder_path(root, -math.inf)
        return count