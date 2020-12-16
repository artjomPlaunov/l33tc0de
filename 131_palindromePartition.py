from collections import defaultdict
import copy

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
            return []
        
        # Build up memo of palindromes
        pals = defaultdict(bool)
        for i in range(len(s)):
            pals[(i,i)] = True
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                pals[(i,i+1)] = True
        for i in range(3, len(s)+1):
            for j in range(0,len(s)-i+1):
                if s[j] == s[j+i-1]:
                    if pals[(j+1,j+i-2)] == True:
                        pals[(j,j+i-1)] = True
                        continue
                pals[(j,j+i-1)] = False
        
        # part[i] contains partitions for substring s[i:]
        part = defaultdict(list)
        part[len(s)-1] = [[s[-1]]]
        part[len(s)] = [[]]
        
        for i in range(len(s)-2, -1,-1):
            for j in range(i, len(s)):
                if pals[(i,j)] == True:
                    tmp = copy.deepcopy(part[j+1])
                    for partition in tmp:
                        partition.append(s[i:j+1])
                        part[i].append(partition)
        
        for partition in part[0]:
            partition.reverse()
        return part[0]
