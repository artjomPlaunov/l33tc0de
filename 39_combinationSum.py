class Solution:
    
    def __init__(self):
        self.res = []
        self.curPath = []
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.DFS(candidates, target)
        return self.res
        
    def DFS(self, candidates, target):
        if len(candidates) == 0:
            return
        num = candidates[0]
        k = target // num
        for i in range(k+1):
            if (i*num) == target:
                newPath = copy.deepcopy(self.curPath)
                for j in range(i):
                    newPath.append(num)
                self.res.append(newPath)
            elif (i*num) > target:
                return
            else:
                for j in range(i):
                    self.curPath.append(num)
                self.DFS(candidates[1:], target-(num*i))
                for j in range(i):
                    self.curPath.pop(-1)
 
 '''
 DP Solution

 from collections import defaultdict

class Solution:
    def combinationSum(self, coins: List[int], target: int) -> List[List[int]]:
        memo = defaultdict(list)
        self.DP(0,target,coins,memo)
        return memo[(0,target)]
        print(memo)

    def DP(self, index, target, coins, memo):
        if (index,target) in memo:
            return
        elif index == len(coins)-1:
            coin = coins[index]
            if target % coin == 0:
                res = []
                k = target//coin
                for i in range(k):
                    res.append(coin)
                memo[(index,target)] = [res]
            return
        coin = coins[index]
        k = target // coin

        for i in range(0,k+1):
            change = target-(i*coin)
            if change == 0:
                res = []
                for i in range(target//coin):
                    res.append(coin)
                memo[(index,target)].append(res)
            else:
                self.DP(index+1,change, coins, memo)
                if memo[(index+1,change)]:
                    for solution in memo[(index+1,change)]:
                        cpy = copy.deepcopy(solution)
                        for j in range(i):
                            cpy.append(coin)
                        memo[(index,target)].append(cpy)
'''
