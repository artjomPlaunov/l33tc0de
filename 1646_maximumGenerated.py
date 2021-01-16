class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        res = 1
        arr = [0,1]
        for x in range(2,n+1):
            i = x//2
            if x % 2 == 0:
                arr.append(arr[i])
            else:
                arr.append(arr[i]+arr[i+1])
            res = max(res, arr[-1])
        return res
