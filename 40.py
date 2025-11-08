class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        from collections import deque
        q = deque([root])
        res = []
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == size - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
