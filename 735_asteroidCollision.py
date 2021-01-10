class Solution:
    
    def reduce(self, S):
        while len(S) >= 2:
            if S[-2] > 0 and S[-1] < 0:
                if abs(S[-1]) == abs(S[-2]):
                    S.pop()
                    S.pop()
                else:
                    if abs(S[-1]) > abs(S[-2]):
                        S[-2] = S[-1]
                        S.pop()
                    else:
                        S.pop()
            else:
                break
        return S
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        S = []
        for num in asteroids:
            if len(S) == 0:
                S.append(num)
                continue

            top = S[-1]
            if top * num < 0:
                S.append(num)
                S = self.reduce(S)
            else:
                S.append(num)
        return S
                
