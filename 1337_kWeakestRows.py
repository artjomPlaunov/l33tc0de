class Solution(object):
    
    def sortKey(self, pair):
        (lst, _) = pair
        res = 0
        for num in lst:
            if num == 1:
                res += 1
            else:
                break
        return res
    
    def kWeakestRows(self, mat, k):
        pairs = []
        i = 0
        for row in mat:
            pairs.append((row,i))
            i += 1
        
        pairs = sorted(pairs, key=self.sortKey)
        
        res = []
        i = 0
        while k > 0:
            (_,idx) = pairs[i]
            res.append(idx)
            i += 1
            k -= 1
        return res
        
