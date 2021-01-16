class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        diff = []
        for i in range(1,len(prices)):
            diff.append(prices[i]-prices[i-1])
        

        l = []
        r = []
        curr,best = 0,0
        for x in diff:
            curr = max(0, curr+x)
            best = max(best,curr)
            l.append(best)
        curr,best = 0,0
        for i in range(len(diff)-1, -1, -1):
            x = diff[i]
            curr = max(0, curr+x)
            best = max(best,curr)
            r.append(best)
        r.reverse()
            
        res = r[0]
        for i in range(len(diff)-1):
            res = max(res, l[i]+r[i+1])
        return res
