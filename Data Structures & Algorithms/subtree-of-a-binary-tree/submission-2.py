class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_is_same(p, q):
            if not p and not q:return True
            if (p and not q) or (q and not p):return False
            if p.val == q.val:
                return check_is_same(p.left, q.left) and check_is_same(p.right, q.right)

        if not root:
            return False
        if not subRoot:
            return True
        if check_is_same(root, subRoot) : return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)