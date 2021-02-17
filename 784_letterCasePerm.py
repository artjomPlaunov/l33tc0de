class Solution(object):
    
    def aux(self, S, idx, res):
        if idx == 0:
            if S[0].isalpha():
                c = S[0]
                res.append(S[0].lower())
                res.append(S[0].upper())
            else:
                res.append(S[0])
        else:
            res = self.aux(S, idx-1, res)
            if S[idx].isalpha():
                original_len = len(res)
                for i in range(original_len):
                    res.append(res[i]+S[idx].lower())
                    res.append(res[i]+S[idx].upper())
            else:
                original_len = len(res)
                for i in range(original_len):
                    res.append(res[i]+S[idx])
        return res
    
    def letterCasePermutation(self, S):
        res = self.aux(S, len(S)-1, [])
        ret = []
        for perm in res:
            if len(perm) == len(S):
                ret.append(perm)
        return ret
