from collections import defaultdict 

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hash = defaultdict(int)
        curMax, res, windowStart = None,0,0
        
        for windowEnd in range(len(s)):
            c = s[windowEnd]
            hash[c] += 1
            if hash[c] > hash[curMax]:
                curMax = c
            curLen = windowEnd-windowStart+1
            
            if curLen - hash[curMax] > k:
                c = s[windowStart] 
                hash[c] -= 1 
                windowStart += 1
                curLen -= 1
            res = max(res,curLen)
        return res
