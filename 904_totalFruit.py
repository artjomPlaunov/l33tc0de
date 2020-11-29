class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        res, windowStart = 0,0
        hash = {}
        
        for windowEnd in range(len(tree)):
            c = tree[windowEnd]
            if c in hash:
                hash[c] += 1
            else:
                hash[c] = 1
            
            while len(hash) > 2:
                c = tree[windowStart]
                if hash[c] > 1:
                    hash[c] -= 1
                else:
                    del hash[c]
                windowStart += 1
            
            l = windowEnd-windowStart+1
            if l > res:
                res = l
        return res
