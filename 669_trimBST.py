# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def aux(self, root, low, high):
        if not root:
            return None
        if root.val >= low and root.val <= high:
            root.left = self.aux(root.left, low, high)
            root.right = self.aux(root.right, low, high)
            return root
        else:
            if root.val < low:
                return self.aux(root.right, low, high)
            elif root.val > high:
                return self.aux(root.left, low, high)
    
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        return self.aux(root, low, high)
