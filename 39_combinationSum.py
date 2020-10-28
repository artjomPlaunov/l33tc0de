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
        
