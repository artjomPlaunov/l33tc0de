# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        S = [(root,1)]
        maxDepth = 1
        while S:
            (node, depth) = S[0]
            if node.left is None and node.right is None and depth > maxDepth:
                maxDepth = depth
            if node.left:
                S.append((node.left,depth+1))
            if node.right:
                S.append((node.right,depth+1))
            S = S[1:]
        return maxDepth
