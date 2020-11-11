# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(nums, 0, len(nums)-1)
        
    def helper(self, nums, lo, hi):
        if hi < lo:
            return None
        mid = (hi+lo)//2
        res = TreeNode(nums[mid], self.helper(nums, lo, mid-1), self.helper(nums, mid+1, hi))
        return res
