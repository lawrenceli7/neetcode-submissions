# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.good = 0

        def dfs(node, check):
            if node.val >= check:
                self.good += 1
            if node.left:
                dfs(node.left, max(node.val, check))
            if node.right:
                dfs(node.right, max(node.val, check))
        dfs(root, root.val)
        return self.good