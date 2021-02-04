from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        # First check that all the characters in word2 are in word1
        contains1 = defaultdict(bool)
        contains2 = defaultdict(bool)
        for c in word1:
            contains1[c] += 1
        for c in word2:
            if contains1[c] == False:
                return False
            contains2[c] += 1
        
        
        set1 = defaultdict(int)
        set2 = defaultdict(int)
        
        
        
        for key in contains1:
            set1[contains1[key]] += 1
        for key in contains2:
            set2[contains2[key]] += 1
              
        for key in set1:
            if set1[key] != set2[key]:
                return False
        return True
    
        
