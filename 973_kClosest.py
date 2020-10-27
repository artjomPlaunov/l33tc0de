import heapq

class Solution:
    def distance(self, x: int, y: int) -> int:
        return math.sqrt((x**2)+(y**2))
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            d = self.distance(point[0],point[1])
            if len(maxHeap) < K:
                heapq.heappush(maxHeap, (-d, point))
            else:
                (curr,_) = maxHeap[0]
                if d <= -curr:
                    heapq.heappushpop(maxHeap, (-d, point))
        
        res = []
        for (_, point) in maxHeap:
            res.append(point)
        return res
