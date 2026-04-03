class BSTSolutions:
    # 1. Minimum Absolute Difference in BST
    def getMinimumDifference(self, root: TreeNode) -> int:
        prev, res = None, float('inf')
        def inorder(node):
            nonlocal prev, res
            if not node: return
            inorder(node.left)
            if prev is not None: res = min(res, node.val - prev)
            prev = node.val
            inorder(node.right)
        inorder(root)
        return res

    # 2. Kth Smallest Element in a BST
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0: return curr.val
            curr = curr.right

    # 3. Validate Binary Search Tree
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, left, right):
            if not node: return True
            if not (left < node.val < right): return False
            return valid(node.left, left, node.val) and \
                valid(node.right, node.val, right)
        return valid(root, float("-inf"), float("inf"))
