# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        
        if root is None:
            return []
        
        Q = collections.deque()
        Q.append(root)
        res = []
        while Q:
            original_len = len(Q)
            res.append(Q[-1].val)
            for i in range(original_len):
                if Q[i].left:
                    Q.append(Q[i].left)
                if Q[i].right:
                    Q.append(Q[i].right)
            for i in range(original_len):
                Q.popleft()
        return res
