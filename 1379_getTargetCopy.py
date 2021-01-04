# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        S = [(original,cloned)]
        while S:
            (o,c) = S[-1]
            S = S[:-1]
            if o.val == target.val:
                return c
            if o.left is not None:
                S.append((o.left,c.left))
            if o.right is not None:
                S.append((o.right,c.right))
