from collections import defaultdict

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        h = defaultdict(list)
        for piece in pieces:
            h[piece[0]] = piece
        
        i = 0
        while i < len(arr):
            piece =  h[arr[i]]
            if piece == []:
                return False
            for num in piece:
                if num != arr[i]:
                    return False
                i += 1
        return True
