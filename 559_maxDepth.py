"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        maxDepth = 1
        S = [(root, 1)]
        
        while S:
            (node, depth) = S[-1]
            S = S[:-1]
            if depth > maxDepth:
                maxDepth = depth
            if node.children is not None:
                for child in node.children:
                    S.append((child, depth+1))
        return maxDepth
