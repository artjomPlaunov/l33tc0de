# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return []
        res, curPath = [], []
        self.helper(root, sum, res, curPath)
        return res
    
    def helper(self, root, sum, res, curPath):
        if root.left is None and root.right is None:
            if root.val - sum == 0:
                newPath = copy.deepcopy(curPath)
                newPath.append(root.val)
                res.append(newPath)
                return
        curPath.append(root.val)
        if root.left:
            self.helper(root.left, sum-root.val, res, curPath)
        if root.right:
            self.helper(root.right, sum-root.val, res, curPath)
        curPath.pop(-1)
