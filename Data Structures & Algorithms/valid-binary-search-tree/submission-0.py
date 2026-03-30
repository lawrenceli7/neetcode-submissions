# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # root has no parent, so it can be any value from -inf to inf
        # when checking left subtree, make sure it is greater than -inf and less than the parent
        # when checking right subtree, make sure it is less than inf and greater than the parent
        # repeat for rest of the nodes
        # basically checking left and right boundaries of nodes

        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            return (valid(node.left, left, node.val) and 
            valid(node.right, node.val, right))

        return valid(root, float("-inf"), float("inf"))