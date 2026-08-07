class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            if abs(leftHeight - rightHeight) > 1:
                res = False

            return 1 + max(leftHeight, rightHeight)

        dfs(root)

        return res