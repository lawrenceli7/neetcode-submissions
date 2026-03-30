# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder, start at the root, process the current node, then the left subtree, then the right subtree
        # inorder, start at the root, take care of the left subtree first, then the root, then the right subtree
        # 1) the first val of the preorder is always the root
        # 2) every val left of the root in the inorder will be in the left subtree, vica versa to the right

        # id preorder or inorder is empty, return null
        if not preorder or not inorder:
            return None

        # creating the root as it is the first val of the preorder
        root = TreeNode(preorder[0])
        # get the index of predorder[0] as everything to the left is in the left subtree and vice versa
        mid = inorder.index(preorder[0])
        # start at index 1 going to mid + 1 for preorder
        # start from the beginning to mid, but not including mid for inorder
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # start at mid + 1 to end of array for preorder
        # start at mid + 1 to end of array for inorder
        root.right = self.buildTree(preorder[mid+1:], inorder[mid + 1:])
        return root





