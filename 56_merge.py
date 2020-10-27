class Solution:
    
    def sortKey(self, interval: List[int]) -> int:
        return interval[0]
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return []
        
        intervals   = sorted(intervals, key=self.sortKey)
        res         = []
        start, end  = intervals[0][0], intervals[0][1]
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] > end:
                res.append([start,end])
                start, end = interval[0], interval[1]
            else:
                start   = min(start, interval[0])
                end     = max(end, interval[1])
        
        res.append([start,end])
        return res
