class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if numCourses == 1:
            return True
        if len(prerequisites) == 0:
            return True
        
        G = [[] for i in range(numCourses)]
        for prereq in prerequisites:
            G[prereq[0]].append(prereq[1])
        
        inDegree = {}
        for prereq in prerequisites:
            if prereq[1] in inDegree:
                inDegree[prereq[1]] += 1
            else:
                inDegree[prereq[1]] = 1
        
        Q = []
        queueMap = {}
        for i in range(numCourses):
            if i in inDegree or i in queueMap:
                continue
            else:
                queueMap[i] = True
                Q.append(i)
        
        if len(Q) == 0:
            return False
        numVisited = 0
        
        while len(Q) > 0:
            u = Q[-1]
            Q = Q[:-1]
            numVisited += 1
            
            for v in G[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    Q.append(v)
        
        if numVisited == numCourses:
            return True
        else:
            return False
