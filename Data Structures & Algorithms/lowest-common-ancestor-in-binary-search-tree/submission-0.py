# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if p and q are in seperate subtrees, that split where it occirs is the LCA
        # the root is an ancestor of everything in the tree

        curr = root

        while curr:
            # if both values are greater than the current value we are visitng, we go right
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # if both values are less than the current value we are visitng, we go left
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # if split occurs or we find one of the values p or q
            else:
                return curr

