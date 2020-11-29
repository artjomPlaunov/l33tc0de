from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = defaultdict(bool)
        res, windowStart = 0,0
        
        for windowEnd in range(len(s)):
            hash[s[windowEnd]] += 1
            
            while hash[s[windowEnd]] > 1:
                hash[s[windowStart]] -= 1
                windowStart += 1
            
            if (windowEnd-windowStart+1) > res:
                res = windowEnd-windowStart+1
        return res
