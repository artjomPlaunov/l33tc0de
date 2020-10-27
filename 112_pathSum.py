# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        S = [(root, sum)]
        while S:
            (node, sum) = S[0]
            S = S[1:]
            if node.left is None and node.right is None:
                if node.val-sum == 0:
                    return True
            if node.left:
                S.append((node.left, sum-node.val))
            if node.right:
                S.append((node.right, sum-node.val))
        return False

