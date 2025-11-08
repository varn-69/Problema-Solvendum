class Solution:
    def binaryTreePaths(self, root):
        res = []
        def dfs(node, path):
            if not node:
                return
            if not node.left and not node.right:
                res.append(path + str(node.val))
            else:
                dfs(node.left, path + str(node.val) + "->")
                dfs(node.right, path + str(node.val) + "->")
        dfs(root, "")
        return res
