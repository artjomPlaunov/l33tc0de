class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res,i,j = 0,0,len(people)-1
        
        while i <= j:
            if i == j:
                return res+1
            elif j-i == 1:
                if people[i] + people[j] > limit:
                    return res+2
                else:
                    return res+1
            else:
                if people[i] + people[j] > limit:
                    res += 1
                    j -= 1
                else:
                    res += 1
                    i += 1
                    j -= 1
