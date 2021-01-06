class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def takeSecond(interval):
            return interval[1]
        
        if len(points) == 0:
            return 0
        points.sort(key=takeSecond)
        res = 0
        
        i = 0
        while i < len(points):
            _,hi = points[i]
            j = i+1
            
            while j < len(points) and points[j][0] <= hi:
                j += 1
            res += 1
            i = j
        return res
            
