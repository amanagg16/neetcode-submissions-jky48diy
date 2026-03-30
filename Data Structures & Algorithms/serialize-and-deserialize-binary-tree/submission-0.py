class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def preorder(root: Optional[TreeNode]) -> None:
            if not root:
                res.append("N")
                return # this is important...in normal preorder we don't return

            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        index = 0
        def helper():
            nonlocal index
            if vals[index] == "N":
                index += 1
                return None
            node = TreeNode(int(vals[index]))
            index += 1
            node.left = helper()
            node.right = helper()
            return node

        return helper()