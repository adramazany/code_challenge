import collections

class TreeBFSSolutions:
    # 1. Binary Tree Right Side View
    def rightSideView(self, root: TreeNode) -> list[int]:
        res = []
        q = collections.deque([root])
        while q:
            rightNode = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    rightNode = node
                    q.append(node.left)
                    q.append(node.right)
            if rightNode: res.append(rightNode.val)
        return res

    # 2. Average of Levels in Binary Tree
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        res = []
        q = collections.deque([root])
        while q:
            level_sum, count = 0, len(q)
            for _ in range(count):
                node = q.popleft()
                level_sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level_sum / count)
        return res

    # 3. Binary Tree Level Order Traversal
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        res = []
        q = collections.deque([root])
        while q:
            val = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    val.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if val: res.append(val)
        return res
