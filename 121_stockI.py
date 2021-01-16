class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = []
        for i in range(1,len(prices)):
            diff.append(prices[i]-prices[i-1])
        
        best = 0
        curr = 0
        
        for x in diff:
            curr = max(0,curr+x)
            best = max(best,curr)
        return best
