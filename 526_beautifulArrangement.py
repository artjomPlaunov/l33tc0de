from collections import defaultdict

class Solution:
    
    def get_key(self, lst):
        return '_'.join(str(num) for num in lst)
  
    def get_lst(self, key):
        if key == '':
            return []
        return list(map(int, key.split('_')))

    def countArrangement(self, n: int) -> int:
        key = self.get_key(list(range(1,n+1)))
        memo = defaultdict(int)
        self.DP(1,n,key,memo)
        return memo[(1,key)]
        
    def DP(self, index, max_index, key, memo):
        if (index,key) in memo:
            return 
        l = self.get_lst(key)
        if index == max_index:
            if l[0] % index == 0 or index % l[0] == 0:
                memo[(index,key)] = 1
                return
        res = 0
        
        for i in range(len(l)):
            num = l[i] 
            if num % index == 0 or index % num == 0:
                cpy = copy.deepcopy(l)
                cpy.pop(i)
                cpy = self.get_key(cpy)
                self.DP(index+1, max_index, cpy, memo)
                
                res += memo[(index+1,cpy)]
        if index > max_index:
            return
        memo[(index,key)] = res
