class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        leftInvert = self.invertTree(root.left)
        rightInvert = self.invertTree(root.right)

        return root