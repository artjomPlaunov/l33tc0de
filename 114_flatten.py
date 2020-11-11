# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if root is None:
            return root
        
        (root, _) = self.helper(root)
        return root
        
    def helper(self, root):
        if root is None:
            return (root,root)
        if root.left is None and root.right is None:
            return (root,root)
        
        (left, end) = self.helper(root.left)
        (right, _end) = self.helper(root.right)
        
        root.left = None
        if left is not None:
            root.right = left
            end.right = right
        else:
            root.right = right
        if _end is not None:
            return (root, _end)
        if end is not None:
            return (root, end)
        
        
