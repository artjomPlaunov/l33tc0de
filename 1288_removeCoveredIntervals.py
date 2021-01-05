class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        lo,hi = intervals[0]
        
        j = 1
        while j < len(intervals):
            _lo,_hi = intervals[j]
            if lo <= _lo and _hi <= hi:
                res += 1
                j += 1
            elif lo == _lo and hi < _hi:
                hi = _hi
                res +=1 
                j += 1
            else:
                lo,hi = intervals[j]
                j += 1
        return len(intervals)-res
