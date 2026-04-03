class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreeSolutions:
    # 1. Maximum Depth of Binary Tree
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # 2. Same Tree
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # 3. Invert Binary Tree
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    # 4. Symmetric Tree
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1, t2):
            if not t1 and not t2: return True
            if not t1 or not t2: return False
            return t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        return isMirror(root, root)

    # 5. Path Sum
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root: return False
        if not root.left and not root.right: return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or \
            self.hasPathSum(root.right, targetSum - root.val)

    # 6. Lowest Common Ancestor
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root
        return left or right
