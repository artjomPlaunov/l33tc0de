class Solution:
    
    def aux(self, cur, n):
        if n == 0:
            return 0
        elif n == 1:
            return 5-cur
        else:
            res = 0
            for i in range(cur, 5):
                res += self.aux(i, n-1)
            return res
    
    def countVowelStrings(self, n: int) -> int:
        cur = 0
        return self.aux(cur,n)
