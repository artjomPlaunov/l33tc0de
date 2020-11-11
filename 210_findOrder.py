from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        G = [[] for i in range(numCourses)]
        inDegrees = defaultdict(int)

        # Populate adjacency lists and indegree counts
        for edge in prerequisites:
            inDegrees[edge[0]] += 1
            G[edge[1]].append(edge[0])

     
        Q = []
        for i in range(numCourses):
            if i not in inDegrees:
                Q.append(i)
        
        while Q:
            u = Q[-1]
            Q = Q[:-1]
            res.append(u)
            
            for v in G[u]:
                inDegrees[v] -= 1
                if inDegrees[v] == 0:
                    Q.append(v)
        if len(res) == numCourses:
            return res
        else:
            return []
