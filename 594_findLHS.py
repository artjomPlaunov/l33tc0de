from collections import defaultdict

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        res = 0
        for num in nums:
            if (num+1) in count:
                res = max(res, count[num]+count[num+1])
        return res
