from collections import defaultdict
from string import ascii_lowercase
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        book = defaultdict(bool)
        for word in wordList:
            book[word] = True
        if endWord not in book:
            return 0
        seen = defaultdict(int)
        seen[beginWord] = 1
        
        Q = deque()
        Q.append(beginWord)
        while Q:
            u = Q.popleft()
            for i in range(len(u)):
                for c in ascii_lowercase:
                    if c == u[i]:
                        continue
                    v = u[:i] + c + u[i+1:]
                    if v == endWord:
                        return seen[u]+1
                    elif v not in seen and book[v] == True:
                        Q.append(v)
                        seen[v] = seen[u]+1
        return 0
