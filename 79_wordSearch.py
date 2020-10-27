from collections import defaultdict

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    memo = defaultdict(bool)
                    if self.DFS(board, word, memo, (i,j)):
                        return True
    
    def DFS(self, board, word, memo, coord):
        if memo[coord] == True:
            return False
        (i,j) = coord
        if len(word) == 1:
            if board[i][j] == word[0]:
                return True
        if word[0] != board[i][j]:
            return False
        
        memo[coord] = True
        coords = [
            [0,1],
            [1,0],
            [-1,0],
            [0,-1]
        ]
         
        for coord in coords:
            x,y = i+coord[0], j+coord[1]
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[x]):
                continue
            if self.DFS(board, word[1:], memo, (x,y)):
                return True
        memo[(i,j)] = False
        return False
