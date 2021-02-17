from collections import defaultdict

class Solution(object):
    
    def isBipartite(self, graph):
        seen = defaultdict(bool)
        Q = deque()
        for u in range(len(graph)):
            if u not in seen:
                seen[u] = True
                Q.append(u)
                while Q:
                    u = Q.popleft()
                    for v in graph[u]:
                        if v in seen:
                            if seen[u] == seen[v]:
                                return False
                        else:
                            seen[v] = not seen[u]
                            Q.append(v)
        return True
