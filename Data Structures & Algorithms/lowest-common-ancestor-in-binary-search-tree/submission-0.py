class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        if p == root or q == root:
            return root

        leftEval = self.lowestCommonAncestor(root.left, p, q)
        rightEval = self.lowestCommonAncestor(root.right, p, q)

        if leftEval and rightEval:
            return root

        if not leftEval:
            return rightEval
        return leftEval