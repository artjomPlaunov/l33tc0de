from collections import defaultdict

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        l = defaultdict(int)
        r = defaultdict(int)
        res = 0
        
        for i in range(len(A)):
            for j in range(len(B)):
                l[A[i]+B[j]] += 1
                r[C[i]+D[j]] += 1
        
        for lkey in l:
            complement = 0-lkey
            if complement in r:
                res += l[lkey] * r[0-lkey]
        return res
